export const codes = {
  error: 400,
  success: 200,
  warning: 300,
  unauthorized: 403
}

export const toasts = {
  position: 'top-right',
  duration: 2000,
  theme: 'bubble'
}

export const regex = {
  phone: /^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\\./0-9]*$/,
  password: /^$|^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/
}

export const oauthConfig = {
  google: {
    oauth2Endpoint: 'https://accounts.google.com/o/oauth2/v2/auth',
    scope: ['profile', 'email'].join(' ')
  }
}
