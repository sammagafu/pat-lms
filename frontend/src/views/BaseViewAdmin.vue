<template>
  <div class="flex flex-row">
    <!-- <p class="text-white">{{ userstore.userData.is_student }}</p> -->
    <aside class="basis-1/5" aria-label="Sidebar">
      <template v-if="userstore.userData.is_student === 'true'">
        <StudentSideBar />
      </template>
      <template v-else-if="userstore.userData.is_tuitor === 'true'">
        <TuitorSideBar />
      </template>
    </aside>
    <div class="basis-4/5 px-16 bg-gray-50 dark:bg-gray-800">
      <RouterView />
    </div>
  </div>
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
// import Sidebar from '@/components/TuitorSidebar.vue';
import StudentSideBar from '@/components/StudentSideBar.vue';
import TuitorSideBar from '@/components/TuitorSideBar.vue'
import { userStore, pagesInteractivity } from '@/stores/index'
import { ref } from 'vue';

export default{
  name:"BaseViewAdmin",
  components : { StudentSideBar,TuitorSideBar },
  setup (){
    const userstore = userStore()
    return{
      userstore
    }
  },
}
</script>