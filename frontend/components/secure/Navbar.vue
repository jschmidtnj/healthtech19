<template>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="/">Home</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/heatmap">Heatmap</b-nav-item>
        <b-nav-item-dropdown right>
          <template slot="button-content">
            <em>User</em>
          </template>
          <b-dropdown-item href="/account">Profile</b-dropdown-item>
          <b-dropdown-item href="#" @click="logout">
            Sign Out
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'AdminNavbar',
  // @ts-ignore
  layout: 'secure',
  computed: {
    loggedin() {
      return this.$store.state.auth && this.$store.state.auth.loggedIn
    }
  },
  methods: {
    logout(evt) {
      evt.preventDefault()
      this.$store.commit('auth/logout')
      if (
        this.$nuxt.$data.layoutName === 'secure' ||
        this.$nuxt.$data.layoutName === 'admin'
      ) {
        this.$router.push({
          path: '/login'
        })
      }
    }
  }
})
</script>

<style lang="scss"></style>
