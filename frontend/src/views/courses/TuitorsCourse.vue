<template>
    <div class="pt-16">
        <h2 class="py-4 font-bold dark:text-gray-400 text-3xl">Course</h2>
        <p class="dark:text-gray-200 text-sm">Manage your courses and its update like live, draft and insight.</p>
    </div>

    <div class="rounded dark:bg-slate-500 bg-gray-100 shadow-md py-6 mt-6">
        <table class="table-auto w-full">
            <thead class="text-xs font-semibold uppercase text-gray-40">
                <tr>
                    <th class="p-2 whitespace-nowrap">
                        <div class="font-semibold text-left">Course Image</div>
                    </th>
                    <th class="p-2 whitespace-nowrap">
                        <div class="font-semibold text-left">Course Name</div>
                    </th>
                    <th class="p-2 whitespace-nowrap">
                        <div class="font-semibold text-left">Enrolled</div>
                    </th>

                    <th class="p-2 whitespace-nowrap">
                        <div class="font-semibold text-left">Price</div>
                    </th>
                    <th class="p-2 whitespace-nowrap">
                        <div class="font-semibold text-center">Status</div>
                    </th>

                    <th class="p-2 whitespace-nowrap">
                        <div class="font-semibold text-center">Actions</div>
                    </th>
                </tr>
            </thead>
            <tbody class="text-sm divide-y divide-gray-100">

                <tr v-for="(course, pk) in course" :key="pk">
                    <td class="p-2 whitespace-nowrap">
                        <div class="flex items-center">
                            <div class="h-auto w-48">
                                <img class="" :src="course.cover" alt="Alex Shatov">
                            </div>
                        </div>
                    </td>
                    <td class="p-2 whitespace-nowrap">
                        <div class="text-left">
                            <p>{{ course.name }}</p>
                            <p>{{ course.description }}</p>
                        </div>
                    </td>

                    <td class="p-2 whitespace-nowrap">
                        <div class="text-left font-medium text-green-500">0</div>
                    </td>

                    <td class="p-2 whitespace-nowrap">
                        <div class="text-left font-medium text-green-500">{{ course.courseprice }}</div>
                    </td>
                    <td class="p-2 whitespace-nowrap">
                        <div class="text-lg text-center">
                            <span v-if="course.is_published"
                                class="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800">Published</span>
                            <span v-else
                                class="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800">Draft</span>
                        </div>
                    </td>
                    <td class="p-2 whitespace-nowrap">
                        <span
                            class="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800">Add Lessons</span>
                        <span
                            class="bg-gray-100 text-gray-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-gray-300">Edit Course</span>
                        <span
                            class="bg-red-100 text-red-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-red-200 dark:text-red-900">Delete</span>
                        <span
                            class="bg-green-100 text-green-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-green-200 dark:text-green-900">Publish</span>

                    </td>
                </tr>

            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { userStore, pagesInteractivity } from '@/stores/index'
export default {
    setup() {
        const course = ref([])

        onMounted(() => {
            axios.get('course/')
                .then(response => {
                    course.value = response.data;
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error);
                });
        })
        return { course, }
    }

}
</script>