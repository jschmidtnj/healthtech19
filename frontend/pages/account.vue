<template>
  <b-card title="Account Page">
    <b-card-text>
      <b-list-group>
        <b-list-group-item>
          Name: {{ $store.state.auth.user.first_name }},
          {{ $store.state.auth.user.last_name }}
        </b-list-group-item>
        <b-list-group-item>
          Date of Diagnosis: {{ $store.state.auth.user.dod }}
        </b-list-group-item>
        <b-list-group-item>
          Gender: {{ $store.state.auth.user.gender }}
        </b-list-group-item>
        <b-list-group-item>
          Medications:
          {{
            $store.state.auth.user.medications
              ? $store.state.auth.user.medications.join(', ')
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
      <b-form class="mt-4 mb-4" @submit="addToMedications">
        <b-form-group
          id="add-heatmap-group"
          label="Add joint pains:"
          label-for="add-heatmap"
          description="Add to heatmap"
        >
          <b-form-input
            id="add-heatmap"
            v-model="form.medication"
            type="text"
            placeholder="Enter heatmap"
            aria-describedby="emailfeedback"
          ></b-form-input>
        </b-form-group>
        <b-button
          variant="primary"
          type="submit"
          class="mt-2"
          :disabled="form.medication.length === 0"
          >Submit</b-button
        >
      </b-form>
    </b-card-text>
    <b-button class="mt-4" variant="primary" @click="logout">Logout</b-button>
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
  data() {
    return {
      form: {
        medication: ''
      }
    }
  },
  mounted() {
    this.updateUserData()
  },
  methods: {
    updateUserData() {
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
    addToMedications(evt) {
      evt.preventDefault()
      this.$axios
        .put('/medications', {
          medication: this.form.medication
        })
        .then(res => {
          if (res.status === 200) {
            this.updateUserData()
          }
        })
        .catch(err => {
          let message = `got error: ${err}`
          if (err.response && err.response.data) {
            message = err.response.data.message
          }
          this.$toasted.global.error({
            message: message
          })
        })
    },
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
