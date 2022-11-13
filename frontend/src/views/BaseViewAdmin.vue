<template>
  <div class="flex flex-row">
    <aside class="basis-1/5" aria-label="Sidebar">
      <p class="text-white">{{ userstore.userData }}</p>
      <StudentSideBarVue />
    </aside>
    <div class="basis-4/5 px-16 bg-gray-50 dark:bg-gray-800">
      <RouterView />
    </div>
  </div>
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
// import Sidebar from '@/components/TuitorSidebar.vue';
import StudentSideBarVue from '@/components/StudentSideBar.vue';
import { userStore, pagesInteractivity } from '@/stores/index'
import { ref } from 'vue';

export default{
  name:"BaseViewAdmin",
  components : { StudentSideBarVue },
  setup (){
    const userstore = userStore()
    return{
      userstore
    }
  },
}
</script>