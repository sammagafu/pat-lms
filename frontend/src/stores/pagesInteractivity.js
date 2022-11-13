
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const pagesInteractivity = defineStore('pagesInteractivity', () => {

  // const count = ref(0)
  
  const isLoading = ref(false)

//   const doubleCount = computed(() => count.value * 2)
//   function increment() {
//     count.value++
//   }

  return { isLoading }
})
