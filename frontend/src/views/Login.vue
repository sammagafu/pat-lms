<template>
  <div class="pt-32">
    <div class="bg-gray-100 w-1/2 py-24 px-24 mx-auto text-gray-800 shadow-md rounded">
      <img src="../assets/images/logo.png" alt="PAT Logo" class="logo mx-auto">
      <h2 class="text-center py-3">Welcome to PAT Learning Management System. <br> Don't have an account yet?
        <router-link :to="{ name: 'register' }" class="text-sky-600">Sign up</router-link>
      </h2>
      <form @submit.prevent="userLogin">
        <!-- Email input -->
        <div class="mb-6">
          <input type="email"
            class="form-control block w-full px-4 py-2 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            placeholder="Email address" v-model="email" />
        </div>

        <!-- Password input -->
        <div class="mb-6">
          <input type="password"
            class="form-control block w-full px-4 py-2 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            placeholder="Password" v-model="password" />
        </div>

        <div class="flex justify-between items-center mb-6">
          <div class="form-group form-check">
            <input type="checkbox"
              class="form-check-input appearance-none h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer"
              id="exampleCheck3" checked />
            <label class="form-check-label inline-block text-gray-800" for="exampleCheck2">Remember me</label>
          </div>
          <a href="#!"
            class="text-blue-600 hover:text-blue-700 focus:text-blue-700 active:text-blue-800 duration-200 transition ease-in-out">Forgot
            password?</a>
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
import { userStore, pagesInteractivity } from '@/stores/index'
import { ref } from 'vue';
import axios from 'axios';
import { useRouter, useRoute } from 'vue-router'


export default {
  setup(){
    const router = useRouter()
    const userstore = userStore()
    const pages  = pagesInteractivity()

    const userdata = ref([])
    const email = ref('')
    const password = ref('')
    

    // obtain jwt Token
    function userLogin(){
      const loginData = {
        email: this.email,
        password: this.password
      }

      axios.post('auth/login/',  loginData ).then(response => {
        axios.defaults.headers.common["Authorization"] = ""
        localStorage.removeItem("token")
        userstore.authToken = response.data.access
        userstore.refreshToken = response.data.refresh
        userstore.isAuthenticated = true
        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
        localStorage.setItem("access", response.data.access)
        localStorage.setItem("refresh", response.data.refresh)


      }).catch(error => {
        console.log(error);
      })
      userstore.getUserData()
      
      router.push({name:'home'})
    }

    return { email, password,userLogin}
  },
  methods: {
    // ...mapActions(userStore,)
  }
}
</script>