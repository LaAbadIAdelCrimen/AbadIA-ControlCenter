<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <button type="button" class="btn btn-primary">{{ this.msg }}</button>
        {{ this.action.action }}
      </div>
      <div class="col">
        <button type="button" class="btn btn-primary">Next State</button>
        {{ this.action.action }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Dump',
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    getGame () {
      const path = 'http://localhost:5000/game'
      axios.get(path)
        .then((res) => {
          this.msg = res.data.game.filename
          this.getAction('0')
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
    getAction (index) {
      const path = 'http://localhost:5000/action/' + index
      axios.get(path)
        .then((res) => {
          this.msg = 'Action Ready'
          this.action = res.data.action
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    }

  },
  created () {
    this.getGame()
  }
}
</script>
