<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
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
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
    getAction (index) {
      const path = 'http://localhost:5000/action/'+index
      axios.get(path)
        .then((res) => {
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
    this.getAction('0')
  }
}
</script>
