<template>
  <b-card title="Account Page">
    <p>user: {{ this.$store.state.auth.user }}</p>
    <p>token: {{ this.$store.state.auth.token }}</p>
    <b-btn @click="logout">Logout</b-btn>
  </b-card>
</template>

<script lang="ts">
import Vue from 'vue'
// @ts-ignore
const seo = JSON.parse(process.env.seoconfig)
export default Vue.extend({
  // @ts-ignore
  layout: 'secure',
  // @ts-ignore
  head() {
    const title = 'Account'
    const description = `your account: ${
      this.$store.state.auth.user
        ? this.$store.state.auth.user.email
        : 'logging out'
    }`
    const image = `${seo.url}/icon.png`
    return {
      title: title,
      meta: [
        { property: 'og:title', content: title },
        { property: 'og:description', content: description },
        {
          property: 'og:image',
          content: image
        },
        { name: 'twitter:title', content: title },
        {
          name: 'twitter:description',
          content: description
        },
        {
          name: 'twitter:image',
          content: image
        },
        { hid: 'description', name: 'description', content: description }
      ]
    }
  },
  methods: {
    logout(evt) {
      evt.preventDefault()
      this.$store.commit('auth/logout')
      this.$router.push({
        path: '/login'
      })
    }
  }
})
</script>

<style lang="scss"></style>
