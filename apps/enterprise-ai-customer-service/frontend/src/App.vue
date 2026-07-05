<script setup lang="ts">
import { computed, ref } from 'vue'

const API_BASE = 'http://127.0.0.1:8000'

const token = ref('')
const username = ref('admin')
const password = ref('admin123')
const error = ref('')
const kbs = ref<any[]>([])
const selectedKb = ref('')
const kbName = ref('员工制度知识库')
const kbDescription = ref('企业员工制度、报销、年假等资料')
const docs = ref<any[]>([])
const file = ref<File | null>(null)
const question = ref('年假怎么算？')
const answer = ref('')
const sources = ref<any[]>([])
const agentTask = ref('帮我查订单 10086 的状态')
const agentResult = ref<any | null>(null)
const usage = ref<any | null>(null)
const toolLogs = ref<any[]>([])

const authed = computed(() => token.value.length > 0)

function headers() {
  return {
    Authorization: `Bearer ${token.value}`,
    'Content-Type': 'application/json'
  }
}

async function login() {
  error.value = ''
  const response = await fetch(`${API_BASE}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: username.value, password: password.value })
  })
  if (!response.ok) {
    error.value = '登录失败'
    return
  }
  const data = await response.json()
  token.value = data.token
  await loadKbs()
  await loadUsage()
}

async function loadKbs() {
  const response = await fetch(`${API_BASE}/api/knowledge-bases`, { headers: headers() })
  kbs.value = await response.json()
  if (!selectedKb.value && kbs.value.length) selectedKb.value = kbs.value[0].id
  if (selectedKb.value) await loadDocs()
}

async function createKb() {
  await fetch(`${API_BASE}/api/knowledge-bases`, {
    method: 'POST',
    headers: headers(),
    body: JSON.stringify({ name: kbName.value, description: kbDescription.value })
  })
  await loadKbs()
}

function onFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  file.value = target.files?.[0] || null
}

async function loadDocs() {
  if (!selectedKb.value) return
  const response = await fetch(`${API_BASE}/api/documents?knowledge_base_id=${selectedKb.value}`, {
    headers: headers()
  })
  docs.value = await response.json()
}

async function uploadDoc() {
  if (!file.value || !selectedKb.value) return
  const formData = new FormData()
  formData.append('file', file.value)
  await fetch(`${API_BASE}/api/documents/upload?knowledge_base_id=${selectedKb.value}`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${token.value}` },
    body: formData
  })
  file.value = null
  await loadDocs()
}

async function ask() {
  if (!selectedKb.value) return
  const response = await fetch(`${API_BASE}/api/chat`, {
    method: 'POST',
    headers: headers(),
    body: JSON.stringify({ knowledge_base_id: selectedKb.value, question: question.value })
  })
  const data = await response.json()
  answer.value = data.answer
  sources.value = data.sources || []
  await loadUsage()
}

async function runAgent() {
  const response = await fetch(`${API_BASE}/api/agent/run`, {
    method: 'POST',
    headers: headers(),
    body: JSON.stringify({ task: agentTask.value })
  })
  agentResult.value = await response.json()
  await loadUsage()
  await loadToolLogs()
}

async function loadUsage() {
  const response = await fetch(`${API_BASE}/api/usage/summary`, { headers: headers() })
  usage.value = await response.json()
}

async function loadToolLogs() {
  const response = await fetch(`${API_BASE}/api/agent/logs`, { headers: headers() })
  toolLogs.value = await response.json()
}
</script>

<template>
  <main class="page">
    <section v-if="!authed" class="login panel">
      <h1>企业知识库智能客服</h1>
      <input v-model="username" placeholder="用户名" />
      <input v-model="password" placeholder="密码" type="password" />
      <button @click="login">登录</button>
      <p v-if="error" class="error">{{ error }}</p>
      <p class="muted">默认账号：admin / admin123</p>
    </section>

    <template v-else>
      <header class="header">
        <div>
          <h1>企业知识库智能客服</h1>
          <p>RAG + Agent + 用量统计教学版综合项目</p>
        </div>
        <div v-if="usage" class="usage">
          <span>请求 {{ usage.requests }}</span>
          <span>输入 {{ usage.input_tokens }}</span>
          <span>输出 {{ usage.output_tokens }}</span>
        </div>
      </header>

      <section class="grid">
        <aside class="panel">
          <h2>知识库</h2>
          <input v-model="kbName" placeholder="知识库名称" />
          <input v-model="kbDescription" placeholder="知识库描述" />
          <button @click="createKb">新建知识库</button>

          <select v-model="selectedKb" @change="loadDocs">
            <option value="">请选择知识库</option>
            <option v-for="kb in kbs" :key="kb.id" :value="kb.id">{{ kb.name }}</option>
          </select>

          <h2>文档</h2>
          <input type="file" accept=".txt,.md,.markdown" @change="onFileChange" />
          <button :disabled="!file || !selectedKb" @click="uploadDoc">上传文档</button>
          <article v-for="doc in docs" :key="doc.id" class="doc">
            <strong>{{ doc.filename }}</strong>
            <span>{{ doc.chunk_count }} 个片段</span>
          </article>
        </aside>

        <section class="panel">
          <h2>智能客服</h2>
          <textarea v-model="question" />
          <button :disabled="!selectedKb" @click="ask">基于知识库回答</button>
          <section v-if="answer" class="answer">
            <h3>回答</h3>
            <p>{{ answer }}</p>
          </section>
          <section v-if="sources.length" class="sources">
            <h3>引用来源</h3>
            <article v-for="source in sources" :key="source.id" class="source">
              <strong>{{ source.filename }}</strong>
              <span>相似度：{{ source.score }}</span>
              <p>{{ source.content }}</p>
            </article>
          </section>
        </section>

        <section class="panel">
          <h2>Agent 工具调用</h2>
          <textarea v-model="agentTask" />
          <button @click="runAgent">运行 Agent</button>
          <pre v-if="agentResult">{{ JSON.stringify(agentResult, null, 2) }}</pre>
          <h3>工具日志</h3>
          <article v-for="log in toolLogs" :key="log.id" class="source">
            <strong>{{ log.tool_name }}</strong>
            <pre>{{ JSON.stringify(log, null, 2) }}</pre>
          </article>
        </section>
      </section>
    </template>
  </main>
</template>

