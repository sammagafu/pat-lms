<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import Sidebar from '@/components/TuitorSidebar.vue';
import TuitorSideBarVue from './components/TuitorSideBar.vue';
import StudentSideBarVue from './components/StudentSideBar.vue';
</script>

<template>
<div class="flex flex-row">
  <aside class="basis-1/5" aria-label="Sidebar">
    <StudentSideBarVue />
  </aside>
  <div class="basis-4/5 px-16 bg-gray-50 dark:bg-gray-800">
    <RouterView />
  </div>
</div>
</template>