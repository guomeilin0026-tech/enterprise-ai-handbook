<script setup lang="ts">
import { onMounted, ref } from 'vue'

interface DocumentInfo {
  id: string
  filename: string
  chunk_count: number
}

interface Source {
  document_id: string
  filename: string
  chunk_id: string
  content: string
  score: number
}

interface ChatResponse {
  answer: string
  sources: Source[]
}

const API_BASE = 'http://127.0.0.1:8000'

const documents = ref<DocumentInfo[]>([])
const selectedFile = ref<File | null>(null)
const question = ref('年假怎么算？')
const answer = ref('')
const sources = ref<Source[]>([])
const loading = ref(false)
const uploading = ref(false)
const error = ref('')

async function loadDocuments() {
  const response = await fetch(`${API_BASE}/api/documents`)
  documents.value = await response.json()
}

function onFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  selectedFile.value = target.files?.[0] || null
}

async function uploadDocument() {
  if (!selectedFile.value) return

  uploading.value = true
  error.value = ''

  try {
    const formData = new FormData()
    formData.append('file', selectedFile.value)

    const response = await fetch(`${API_BASE}/api/documents/upload`, {
      method: 'POST',
      body: formData
    })

    if (!response.ok) {
      const data = await response.json().catch(() => null)
      throw new Error(data?.detail || '上传失败')
    }

    selectedFile.value = null
    await loadDocuments()
  } catch (err) {
    error.value = (err as Error).message
  } finally {
    uploading.value = false
  }
}

async function deleteDocument(id: string) {
  if (!confirm('确定删除这个文档吗？')) return

  await fetch(`${API_BASE}/api/documents/${id}`, {
    method: 'DELETE'
  })
  await loadDocuments()
}

async function askQuestion() {
  if (!question.value.trim()) return

  loading.value = true
  error.value = ''
  answer.value = ''
  sources.value = []

  try {
    const response = await fetch(`${API_BASE}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        question: question.value
      })
    })

    if (!response.ok) {
      const data = await response.json().catch(() => null)
      throw new Error(data?.detail || '问答失败')
    }

    const data = (await response.json()) as ChatResponse
    answer.value = data.answer
    sources.value = data.sources
  } catch (err) {
    error.value = (err as Error).message
  } finally {
    loading.value = false
  }
}

onMounted(loadDocuments)
</script>

<template>
  <main class="page">
    <header class="header">
      <h1>个人知识库问答系统</h1>
      <p>教学版 RAG：上传文档，系统检索相关片段，再基于资料回答。</p>
    </header>

    <section class="layout">
      <aside class="panel">
        <h2>文档管理</h2>
        <div class="upload">
          <input type="file" accept=".txt,.md,.markdown" @change="onFileChange" />
          <button :disabled="!selectedFile || uploading" @click="uploadDocument">
            {{ uploading ? '上传中...' : '上传文档' }}
          </button>
        </div>

        <p class="hint">支持 UTF-8 编码的 txt、md、markdown 文件。</p>

        <div class="documents">
          <article v-for="doc in documents" :key="doc.id" class="doc">
            <div>
              <strong>{{ doc.filename }}</strong>
              <span>{{ doc.chunk_count }} 个片段</span>
            </div>
            <button class="text" @click="deleteDocument(doc.id)">删除</button>
          </article>
          <p v-if="documents.length === 0" class="empty">还没有上传文档。</p>
        </div>
      </aside>

      <section class="panel qa">
        <h2>知识库问答</h2>
        <textarea v-model="question" placeholder="请输入你的问题" />
        <button :disabled="loading || !question.trim()" @click="askQuestion">
          {{ loading ? '检索中...' : '提问' }}
        </button>

        <p v-if="error" class="error">{{ error }}</p>

        <section v-if="answer" class="answer">
          <h3>回答</h3>
          <p>{{ answer }}</p>
        </section>

        <section v-if="sources.length" class="sources">
          <h3>引用来源</h3>
          <article v-for="source in sources" :key="source.chunk_id" class="source">
            <div class="source-meta">
              <strong>{{ source.filename }}</strong>
              <span>相似度：{{ source.score }}</span>
            </div>
            <p>{{ source.content }}</p>
          </article>
        </section>
      </section>
    </section>
  </main>
</template>

