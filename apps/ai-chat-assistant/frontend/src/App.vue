<script setup lang="ts">
import { computed, nextTick, ref } from 'vue'

type Role = 'user' | 'assistant'

interface ChatMessage {
  role: Role
  content: string
}

const API_BASE = 'http://127.0.0.1:8000'

const input = ref('')
const loading = ref(false)
const error = ref('')
const messages = ref<ChatMessage[]>([
  {
    role: 'assistant',
    content: '你好，我是 AI 聊天助手。你可以先问我：什么是企业 AI 应用？'
  }
])
const abortController = ref<AbortController | null>(null)
const messageListRef = ref<HTMLElement | null>(null)

const canSend = computed(() => input.value.trim().length > 0 && !loading.value)

function scrollToBottom() {
  nextTick(() => {
    const el = messageListRef.value
    if (el) {
      el.scrollTop = el.scrollHeight
    }
  })
}

function buildHistory() {
  return messages.value
    .filter((item) => item.content.trim())
    .slice(-10)
    .map((item) => ({
      role: item.role,
      content: item.content
    }))
}

async function sendStreamMessage() {
  if (!canSend.value) return

  const userMessage = input.value.trim()
  input.value = ''
  error.value = ''
  loading.value = true

  messages.value.push({ role: 'user', content: userMessage })
  const assistantMessage: ChatMessage = { role: 'assistant', content: '' }
  messages.value.push(assistantMessage)
  scrollToBottom()

  abortController.value = new AbortController()

  try {
    const response = await fetch(`${API_BASE}/api/chat/stream`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: userMessage,
        history: buildHistory()
      }),
      signal: abortController.value.signal
    })

    if (!response.ok || !response.body) {
      throw new Error('请求失败，请检查后端是否启动')
    }

    const reader = response.body.getReader()
    const decoder = new TextDecoder('utf-8')

    while (true) {
      const { value, done } = await reader.read()
      if (done) break

      assistantMessage.content += decoder.decode(value, { stream: true })
      scrollToBottom()
    }
  } catch (err) {
    if ((err as Error).name !== 'AbortError') {
      error.value = (err as Error).message || '请求失败'
      assistantMessage.content = '抱歉，请求失败了。'
    }
  } finally {
    loading.value = false
    abortController.value = null
  }
}

function stopGenerate() {
  abortController.value?.abort()
  loading.value = false
}

function clearMessages() {
  if (loading.value) return
  messages.value = [
    {
      role: 'assistant',
      content: '会话已清空。你可以继续提问。'
    }
  ]
}
</script>

<template>
  <main class="page">
    <section class="shell">
      <header class="header">
        <div>
          <h1>AI 聊天助手</h1>
          <p>Vue3 + FastAPI + 大模型 API 最小闭环项目</p>
        </div>
        <button class="ghost" :disabled="loading" @click="clearMessages">清空</button>
      </header>

      <div ref="messageListRef" class="messages">
        <article
          v-for="(message, index) in messages"
          :key="index"
          class="message"
          :class="message.role"
        >
          <div class="role">{{ message.role === 'user' ? '你' : 'AI' }}</div>
          <div class="bubble">{{ message.content || '思考中...' }}</div>
        </article>
      </div>

      <p v-if="error" class="error">{{ error }}</p>

      <footer class="composer">
        <textarea
          v-model="input"
          placeholder="输入你的问题，例如：什么是 RAG？"
          :disabled="loading"
          @keydown.enter.exact.prevent="sendStreamMessage"
        />
        <button v-if="!loading" :disabled="!canSend" @click="sendStreamMessage">发送</button>
        <button v-else class="danger" @click="stopGenerate">停止</button>
      </footer>
    </section>
  </main>
</template>

