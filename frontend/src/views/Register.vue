<template>
  <div class="pt-32">
    <div class="dark:bg-slate-500 w-1/2 py-6 px-24 mx-auto text-slate-900 dark:text-gray-100 shadow-md rounded">
      <img src="../assets/images/logo.png" alt="PAT Logo" class="logo mx-auto">
      <h2 class="text-center py-4">Welcome to PAT Learning Management System. <br> Already have an account? <router-link
          :to="{ name: 'login' }" class="text-sky-600">Login</router-link>
      </h2>
      <form @submit.prevent="regusterUsers">
        <!-- Email input -->
        <div class="mb-6">
          <label for="fullname">Full name</label>
          <input id="fullname" type="text"
            class="form-control block w-full px-4 py-2 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            placeholder="Enter your full name" v-model="fullname" />
        </div>

        <div class="mb-6">
          <label for="email" class="text-gray-300">email</label>
          <input id="email" type="text"
            class="form-control block w-full px-4 py-2 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            placeholder="Enter your e-mail" v-model="email" />
        </div>

                <!-- Password input -->
        <div class="mb-6">
          <label for="password" class="text-gray-300">Password</label>
          <input id="password" type="password"
            class="form-control block w-full px-4 py-2 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            placeholder="Password" v-model="password"/>
        </div>

        <div class="mb-6">
          <label for="phone" class="text-gray-300">Phone Number </label>
          <input id="phone" type="text"
            class="form-control block w-full px-4 py-2 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            placeholder="+2557884111111" v-model="phone"/>
          <p class="text-xs text-gray-400">start with +255 or any country code</p>
        </div>

        <div class="mb-6">
          <label for="mct" class="text-gray-300">MCT Number</label>
          <input id="mct" type="text"
            class="form-control block w-full px-4 py-2 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            placeholder="Enter your MCT" v-model="mct"/>
          <p class="text-xs text-red-500">For doctors only</p>
        </div>

                <!-- Password input -->
        <div class="mb-6">
          <label for="avatar" class="text-gray-300 block">avatar</label>
          <input id="avatar" type="file" ref="avatar" @change="onFileChange"/>
        </div>



        <!-- Submit button -->
        <button type="submit"
          class="inline-block px-7 py-3 bg-blue-600 text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out w-full"
          data-mdb-ripple="true" data-mdb-ripple-color="light">
          Sign in
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.logo {
  width: 120px;
}
</style>

<script>
import { ref } from 'vue';
import axios from 'axios';
export default {
  setup(){
    const fullname =  ref('')
    const email =  ref('')
    const password =  ref('')
    const phone =  ref('')
    const mct =  ref('')
    const avatar =  ref(null)
    const student = ref(true)
    const tuitor = ref(false)


  const onFileChange = (e) => {
      avatar.value = e.target.files[0];
    };
  
  function regusterUsers (){
    const headers = { 
      'Content-Type': 'multipart/form-data',
  
  };
    const formdata = new FormData();
    formdata.append('avatar',avatar.value)
    formdata.append('email',email.value)
    formdata.append('full_name',fullname.value)
    formdata.append('password',password.value)
    formdata.append('phone',phone.value)
    formdata.append('mctnumber',mct.value)
    formdata.append('is_student',student.value)
    formdata.append('is_tuitor',tuitor.value)

    axios.post('auth/register/',formdata,headers).then(response =>{
      
    }).catch(error =>{})
    fullname.value = ''
    email.value = ''
    password.value = ''
    phone.value = ''
    mct.value = ''
    avatar.value = ''
    student.value = ''
    tuitor.value = ''
  }
    return {
      fullname,email,password,phone,mct,avatar,student,tuitor,regusterUsers,onFileChange,
    }
  }
}
</script>
