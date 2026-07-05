<script setup lang="ts">
import { computed, ref } from 'vue'

interface ResumeAnalysis {
  score: number
  strengths: string[]
  weaknesses: string[]
  suggestions: string[]
  rewritten_summary: string
  interview_questions: string[]
}

const API_BASE = 'http://127.0.0.1:8000'

const resume = ref(
  '我是一名前端开发，熟悉 Vue3、组件化开发、接口联调，做过后台管理系统。正在学习 Python FastAPI 和大模型应用开发。'
)
const jobDescription = ref(
  '岗位要求：熟悉 Vue3，有后端接口经验，了解大模型 API、Prompt 工程、RAG 知识库，有 AI 应用项目经验优先。'
)
const loading = ref(false)
const error = ref('')
const result = ref<ResumeAnalysis | null>(null)

const canAnalyze = computed(
  () => resume.value.trim().length >= 10 && jobDescription.value.trim().length >= 10 && !loading.value
)

async function analyzeResume() {
  if (!canAnalyze.value) return

  loading.value = true
  error.value = ''
  result.value = null

  try {
    const response = await fetch(`${API_BASE}/api/resume/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        resume: resume.value,
        job_description: jobDescription.value
      })
    })

    if (!response.ok) {
      const data = await response.json().catch(() => null)
      throw new Error(data?.detail || '分析失败，请检查后端是否启动')
    }

    result.value = await response.json()
  } catch (err) {
    error.value = (err as Error).message || '分析失败'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <main class="page">
    <header class="topbar">
      <div>
        <h1>AI 简历优化助手</h1>
        <p>Prompt Engineering + Structured Output 实战项目</p>
      </div>
      <button :disabled="!canAnalyze" @click="analyzeResume">
        {{ loading ? '分析中...' : '开始分析' }}
      </button>
    </header>

    <section class="workspace">
      <section class="panel editor">
        <label>
          <span>候选人简历</span>
          <textarea v-model="resume" :disabled="loading" />
        </label>

        <label>
          <span>岗位 JD</span>
          <textarea v-model="jobDescription" :disabled="loading" />
        </label>
      </section>

      <section class="panel result">
        <p v-if="error" class="error">{{ error }}</p>

        <div v-if="!result && !error" class="empty">
          输入简历和岗位 JD 后，点击开始分析。
        </div>

        <template v-if="result">
          <section class="score">
            <span>匹配度</span>
            <strong>{{ result.score }}</strong>
          </section>

          <section class="card">
            <h2>优势</h2>
            <ul>
              <li v-for="item in result.strengths" :key="item">{{ item }}</li>
            </ul>
          </section>

          <section class="card">
            <h2>不足</h2>
            <ul>
              <li v-for="item in result.weaknesses" :key="item">{{ item }}</li>
            </ul>
          </section>

          <section class="card">
            <h2>修改建议</h2>
            <ul>
              <li v-for="item in result.suggestions" :key="item">{{ item }}</li>
            </ul>
          </section>

          <section class="card">
            <h2>优化后的个人总结</h2>
            <p>{{ result.rewritten_summary }}</p>
          </section>

          <section class="card">
            <h2>可能的面试问题</h2>
            <ul>
              <li v-for="item in result.interview_questions" :key="item">{{ item }}</li>
            </ul>
          </section>
        </template>
      </section>
    </section>
  </main>
</template>

