<template>
  <b-container>
    <b-jumbotron header="Re Joint" class="mt-4" />
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue'
// @ts-ignore
const seo = JSON.parse(process.env.seoconfig)
export default Vue.extend({
  data() {
    return {}
  },
  // @ts-ignore
  head() {
    const title = 'Home'
    const description = 'provide support for people with arthritis'
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
      ],
      __dangerouslyDisableSanitizers: ['script'],
      script: [
        {
          innerHTML: JSON.stringify({
            '@context': 'http://schema.org',
            '@type': 'WebPage',
            name: title,
            description: description
          }),
          type: 'application/ld+json'
        }
      ]
    }
  },
  mounted() {}
})
</script>

<style lang="scss"></style>
