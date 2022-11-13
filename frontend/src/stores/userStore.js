import {
  ref,
  computed
} from 'vue'
import {
  defineStore
} from 'pinia'
import axios from 'axios'

export const userStore = defineStore({
  id: 'userdata',

  state: () => ({
    authToken: localStorage.getItem('access'),
    refreshToken: localStorage.getItem('refresh'),
    userData: {
      id: localStorage.getItem('userID'),
      email: localStorage.getItem('email'),
      full_name: localStorage.getItem('full_name'),
      phone: localStorage.getItem('phone'),
      is_student: localStorage.getItem('is_student'),
      is_tuitor: localStorage.getItem('is_tuitor'),
      mctnumber: localStorage.getItem('mctnumber'),
      avatar: localStorage.getItem('avatar'),
    },
  }),
  getters: {
    // getAuthToken : (state) =
    doubleCount: (state) => state.counter * 2
  },
  actions: {
    setUser(user) {
      this.userData = user
    },

    getUserData() {
      axios.get('auth/users/me/', {
        headers: {
          "Authorization": `Bearer ${this.authToken}`
        }
      }).then(response => {
        this.setUser({
          'userID': response.data.pk,
          'email': response.data.email,
          'is_staff': response.data.is_staff,
          'full_name': response.data.full_name,
          'phone': response.data.phone,
          'is_student': response.data.is_student,
          'is_tuitor': response.data.is_tuitor,
          'mctnumber': response.data.mctnumber,
          'avatar': response.data.avatar,
        })
        localStorage.setItem('email', response.data.email)
        localStorage.setItem('userID', response.data.pk)
        localStorage.setItem('full_name', response.data.full_name)
        localStorage.setItem('phone', response.data.phone)
        localStorage.setItem('is_student', response.data.is_student)
        localStorage.setItem('is_tuitor', response.data.is_tuitor)
        localStorage.setItem('mctnumber', response.data.mctnumber)
        localStorage.setItem('avatar', response.data.avatar)
      }).catch(error => {
        console.log(error)
      })
    },

    logoutUser() {
      this.user = null;
      this.isAuthenticated = false
      localStorage.removeItem("token");
      localStorage.removeItem("userid");
      localStorage.removeItem("email");
      this.$router.push('/account/login')
    }
  }
})


// isAuthenticated: false,
//     isLoading: false,
//     authToken: JSON.parse(localStorage.getItem('access')),
//     refreshToken: JSON.parse(localStorage.getItem('refresh')),
//     userData: {
//       id: localStorage.getItem('userID'),
//       email: localStorage.getItem('email'),
//       full_name: localStorage.getItem('full_name'),
//       phone: localStorage.getItem('phone'),
//       is_student: localStorage.getItem('is_student'),
//       is_tuitor: localStorage.getItem('is_tuitor'),
//       mctnumber: localStorage.getItem('mctnumber'),
//       avatar: localStorage.getItem('avatar'),
//     },