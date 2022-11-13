<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import Sidebar from '@/components/TuitorSidebar.vue';
import StudentSideBarVue from '@/components/StudentSideBar.vue';
</script>

<template>
<div class="bg-[url('@/assets/images/background/cover.jpg')] h-screen bg-center	bg-no-repeat bg-cover dark:bg-gray-800">
  <div class="px-16">
    <RouterView />
  </div>
</div>
</template>