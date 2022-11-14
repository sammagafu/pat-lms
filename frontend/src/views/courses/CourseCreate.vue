<template>
    <div class="pt-16">
        <h2 class="py-4 font-bold dark:text-gray-400 text-3xl">Create Course</h2>
    </div>
    <div class="rounded dark:bg-slate-500 bg-gray-100 shadow-md py-6 mt-6">
        <form @submit.prevent="addCourse" class="lg:mx-16 md:mx-6" id="registerCourse">
            <div class="mb-6">
                <label for="coursename" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Course Name</label>
                <input type="text" id="coursename"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="course name" required v-model="coursename">
            </div>

            <div class="mb-6">
                <label for="courseDescription" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Course Description</label>
                <textarea name="description" id="courseDescription" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" v-model="description"></textarea>
            </div>

            <div class="mb-6">
                <label for="coursePrice" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Course Price (in TZS)</label>
                <input type="text" id="coursePrice"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    required placeholder="200000" v-model="courseprice">
            </div>
        <div class="mb-6">
          <label for="course" class="text-gray-300 block">Course Cover Image</label>
          <input id="course" type="file" ref="course" @change="handleFileUpload"/>
        </div>
            <button type="submit"
                class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create Course</button>
        </form>
    </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { userStore } from '@/stores/index'

export default{
    setup(){

        const userstore = userStore()
        const coursename = ref('')
        const description = ref('')
        const courseprice = ref('')
        const coverImage = ref(null)

        const handleFileUpload = (e)=>{
            // const = document.querySelector('#file')
            var imagefile = document.querySelector('#registerCourse');
            coverImage.value = e.target.files[0]

        };

        function addCourse(){
            const headers = { 
                'Content-Type': 'multipart/form-data',
                "Authorization" : `Bearer ${userstore.authToken}`
            
            };
            console.log(headers);
            const formData = new FormData();
            formData.append('name',coursename.value)
            formData.append('cover',coverImage.value)
            formData.append('description',description.value)
            formData.append('courseprice',courseprice.value)
            console.log(formData);

            axios.post('course/', formData, { headers }).then(response => {}).catch(error => {
                console.log(error)
            })
            coursename.value = ''
            description.value = ''
            courseprice.value = ''
            coverImage.value = ''
        }



        return { coursename,description, courseprice,addCourse,handleFileUpload }
    }
}
</script>