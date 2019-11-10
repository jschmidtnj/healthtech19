<template>
  <b-card title="Sign up" footer-tag="footer">
    <b-form @submit="signup" @reset="reset">
      <b-form-group
        id="email-address-group"
        label="Email address:"
        label-for="email-address"
        description="Your email is safe with us"
      >
        <b-form-input
          id="email-address"
          v-model="form.email"
          type="text"
          autocomplete="off"
          :state="!$v.form.email.$invalid"
          placeholder="Enter email"
          aria-describedby="emailfeedback"
        ></b-form-input>
        <b-form-invalid-feedback
          id="emailfeedback"
          :state="!$v.form.email.$invalid"
        >
          <div v-if="!$v.form.email.required">email is required</div>
          <div v-else-if="!$v.form.email.email">email is invalid</div>
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group
        id="first-name-group"
        label="First Name:"
        label-for="first-name"
      >
        <b-form-input
          id="first-name"
          v-model="form.first_name"
          type="text"
          autocomplete="on"
          :state="!$v.form.first_name.$invalid"
          placeholder="Enter first name"
          aria-describedby="firstnamefeedback"
        ></b-form-input>
        <b-form-invalid-feedback
          id="firstnamefeedback"
          :state="!$v.form.first_name.$invalid"
        >
          <div v-if="!$v.form.first_name.required">first name is required</div>
          <div v-else-if="!$v.form.first_name.minLength">
            first name must have at least
            {{ $v.form.first_name.$params.minLength.min }} characters
          </div>
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group
        id="last-name-group"
        label="Last Name:"
        label-for="last-name"
      >
        <b-form-input
          id="last-name"
          v-model="form.last_name"
          type="text"
          autocomplete="on"
          :state="!$v.form.last_name.$invalid"
          placeholder="Enter last name"
          aria-describedby="lastnamefeedback"
        ></b-form-input>
        <b-form-invalid-feedback
          id="lastnamefeedback"
          :state="!$v.form.last_name.$invalid"
        >
          <div v-if="!$v.form.last_name.required">last name is required</div>
          <div v-else-if="!$v.form.last_name.minLength">
            last name must have at least
            {{ $v.form.last_name.$params.minLength.min }} characters
          </div>
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group
        id="date-of-birth-group"
        label="Date of Birth:"
        label-for="date-of-birth"
      >
        <b-form-input
          id="date-of-birth"
          v-model="form.dob"
          type="date"
          autocomplete="on"
          :state="!$v.form.dob.$invalid"
          placeholder="Enter date of birth"
          aria-describedby="dateofbirthfeedback"
        ></b-form-input>
        <b-form-invalid-feedback
          id="dateofbirthfeedback"
          :state="!$v.form.dob.$invalid"
        >
          <div v-if="!$v.form.dob.required">date of birth is required</div>
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group
        id="phone-number-group"
        label="Phone Number:"
        label-for="phone-number"
      >
        <b-form-input
          id="phone-number"
          v-model="form.phone"
          type="tel"
          autocomplete="on"
          :state="!$v.form.phone.$invalid"
          placeholder="Enter phone number"
          aria-describedby="phonefeedback"
        ></b-form-input>
        <b-form-invalid-feedback
          id="phonefeedback"
          :state="!$v.form.phone.$invalid"
        >
          <div v-if="!$v.form.phone.required">phone is required</div>
          <div v-else-if="!$v.form.phone.validPhone">phone is invalid</div>
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group id="gender-group" label="Gender:" label-for="gender">
        <b-form-radio v-model="form.gender" name="male-radio" value="male"
          >Male</b-form-radio
        >
        <b-form-radio v-model="form.gender" name="female-radios" value="female"
          >Female</b-form-radio
        >
        <b-form-invalid-feedback
          id="genderfeedback"
          :state="!$v.form.phone.$invalid"
        >
          <div v-if="!$v.form.gender.required">gender is required</div>
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group
        id="diagnosis-date-group"
        label="Date of Diagnosis"
        label-for="diagnosis-date"
      >
        <b-form-input
          id="diagnosis-date"
          v-model="form.dod"
          type="date"
          autocomplete="off"
          :state="!$v.form.dod.$invalid"
          aria-describedby="dateofdiagnosisfeedback"
        ></b-form-input>
        <b-form-invalid-feedback
          id="dateofdiagnosisfeedback"
          :state="!$v.form.dod.$invalid"
        >
          <div v-if="!$v.form.dod.required">date of diagnosis is required</div>
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group
        id="password-group"
        label="Password:"
        label-for="password"
        description="Password must be at least 8 characters long, with a number, capital letter and special character"
      >
        <b-form-input
          id="password"
          v-model="form.password"
          type="password"
          autocomplete="off"
          :state="!$v.form.password.$invalid"
          placeholder="Enter password"
          aria-describedby="passwordfeedback"
        ></b-form-input>
        <b-form-invalid-feedback
          id="passwordfeedback"
          :state="!$v.form.password.$invalid"
        >
          <div v-if="!$v.form.password.required">password is required</div>
          <div v-else-if="!$v.form.password.validPassword">
            password is invalid
          </div>
        </b-form-invalid-feedback>
      </b-form-group>
      <b-button
        variant="primary"
        type="submit"
        class="mt-4"
        :disabled="$v.form.$invalid"
        >Submit</b-button
      >
    </b-form>
    <p slot="footer">
      By clicking submit you aggree to the
      <a href="/privacy">privacy policy</a>. This site is protected by reCAPTCHA
      and the Google
      <a href="https://policies.google.com/privacy">Privacy Policy</a> and
      <a href="https://policies.google.com/terms">Terms of Service</a> apply.
    </p>
  </b-card>
</template>

<script lang="ts">
import Vue from 'vue'
import { validationMixin } from 'vuelidate'
import { required, email, minLength } from 'vuelidate/lib/validators'
import { regex } from '~/assets/config'
const validPhone = val => regex.phone.test(val)
const validPassword = val => regex.password.test(val)
// @ts-ignore
const seo = JSON.parse(process.env.seoconfig)
export default Vue.extend({
  name: 'SignUp',
  mixins: [validationMixin],
  data() {
    return {
      form: {
        email: '',
        first_name: '',
        last_name: '',
        phone: '',
        gender: '',
        dob: '', // date of birth
        dod: '', // date of diagnosis
        password: ''
      }
    }
  },
  // @ts-ignore
  validations: {
    form: {
      email: {
        required,
        email
      },
      first_name: {
        required,
        minLength: minLength(3)
      },
      last_name: {
        required,
        minLength: minLength(3)
      },
      phone: {
        required,
        validPhone: validPhone
      },
      gender: {
        required
      },
      dob: {
        required
      },
      dod: {
        required
      },
      password: {
        required,
        validPassword
      }
    }
  },
  // @ts-ignore
  head() {
    const title = 'Sign Up'
    const description = 'sign up for an account'
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
    reset(evt) {
      evt.preventDefault()
      this.form = {
        email: '',
        password: ''
      }
    },
    signup(evt) {
      evt.preventDefault()
      this.$recaptcha('login')
        .then(recaptchatoken => {
          this.$axios
            .post('/register', {
              email: this.form.email,
              password: this.form.password,
              first_name: this.form.first_name,
              last_name: this.form.last_name,
              dob: this.form.dob,
              dod: this.form.dod,
              phone: this.form.phone,
              gender: this.form.gender,
              recaptcha: recaptchatoken
            })
            .then(res => {
              if (res.status === 200) {
                if (res.data) {
                  let message = 'finished signing up.'
                  if (res.data.message) {
                    message = res.data.message
                  }
                  this.$toasted.global.success({
                    message: message
                  })
                  this.reset(evt)
                  setTimeout(() => {
                    this.$router.push({
                      path: '/login'
                    })
                  }, 1000)
                } else {
                  this.$toasted.global.error({
                    message: 'could not get data'
                  })
                }
              } else if (res.data && res.data.message) {
                this.$toasted.global.error({
                  message: res.data.message
                })
              } else {
                this.$toasted.global.error({
                  message: `status code of ${res.status}`
                })
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
        })
        .catch(err => {
          this.$toasted.global.error({
            message: `got error with recaptcha ${err}`
          })
        })
    }
  }
})
</script>

<style lang="scss"></style>
