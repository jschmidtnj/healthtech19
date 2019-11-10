<template>
  <b-container>
    <div class="main-container">
      <b-img class="heatmap" src="~/static/human.png"></b-img>
      <b-img
        v-for="(name, index) in $store.state.auth.user.heatmap"
        :key="index"
        src="~/static/orange.png"
        class="heatspot"
        :style="getStyle(name)"
      ></b-img>
    </div>
    <b-form add-class="mt-4" @submit="addToHeatmap">
      <b-form-group
        id="add-heatmap-group"
        label="Add joint pains:"
        label-for="add-heatmap"
        description="Add to heatmap"
      >
        <b-form-input
          id="add-heatmap"
          v-model="form.location"
          type="text"
          placeholder="Enter heatmap"
        ></b-form-input>
      </b-form-group>
      <b-button
        variant="primary"
        type="submit"
        class="mt-4"
        :disabled="form.location.length === 0"
        >Submit</b-button
      >
    </b-form>
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue'
// @ts-ignore
const seo = JSON.parse(process.env.seoconfig)
export default Vue.extend({
  name: 'Heatmap',
  // @ts-ignore
  head() {
    const title = 'About'
    const description =
      'supports people who have arthritis with managing time and tracking symptoms'
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
        location: ''
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
    getSrc(name) {
      console.log(name)
      return 'orange.png'
    },
    getStyle(name) {
      let left = window.innerWidth / 2
      console.log(left)
      if (name === 'left knee')
        return {
          top: '10rem',
          'text-align': 'center',
          transform: 'translateX(50%)'
        }
      if (name === 'right knee')
        return {
          top: '60px',
          left: '80px'
        }
    },
    addToHeatmap(evt) {
      evt.preventDefault()
      this.$axios
        .post('/heatmap', {
          location: this.form.location
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
    }
  }
})
</script>

<style lang="scss">
.main-container {
  position: relative;
  margin-top: 2rem;
}
.heatmap {
  max-height: 30rem;
  display: block;
  margin:auto;
  position: relative;
}
.heatspot {
  height: 5rem;
  position: absolute;
}
</style>
