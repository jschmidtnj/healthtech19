<template>
  <b-card title="Account Page">
    <p></p>
    <b-card-text>
      <b-list-group>
        <b-list-group-item>
          Name: {{ this.$store.state.auth.user.first_name }},
          {{ this.$store.state.auth.user.last_name }}
        </b-list-group-item>
        <b-list-group-item>
          Date of Diagnosis: {{ this.$store.state.auth.user.dod }}
        </b-list-group-item>
        <b-list-group-item>
          Gender: {{ this.$store.state.auth.user.gender }}
        </b-list-group-item>
        <b-list-group-item>
          Medications:
          {{
            this.$store.state.auth.user.medications
              ? this.$store.state.auth.user.medications.join(', ')
              : ''
          }}
        </b-list-group-item>
        <b-list-group-item>
          Heat Map:
          {{
            this.$store.state.auth.user.heatmap
              ? this.$store.state.auth.user.heatmap.join(', ')
              : ''
          }}
        </b-list-group-item>
      </b-list-group>
    </b-card-text>
    <b-button variant="primary" @click="logout">Logout</b-button>
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
  mounted() {
    /* eslint-disable */
    this.$store
      .dispatch('auth/getUser')
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.error(err)
      })
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
