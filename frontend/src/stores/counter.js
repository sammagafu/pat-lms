import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('userStore', () => {

  // const count = ref(0)
  const isLoading  = ref(false)
  isAuthenticated = ref(false)

  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
