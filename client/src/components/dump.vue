<template>
  <div class="container">
    <div class="row">
      <div class="col">
        {{ this.msg }}
      </div>
    </div>
    <div class="row">
      <div class="col">
        <button type="button" class="btn btn-primary">State</button> <br/>
        Día: {{ this.state.dia }} Hora: {{ this.state.momentoDia }} Pantalla: {{ this.state.numPantalla }}<br/>
        Obsequium: {{ this.state.obsequium }} Bonus: {{ this.state.bonus }} Porcentaje: {{ this.state.procentaje }} <br/>
        {{ this.action.action }} <br/>
        {{ this.action.action }} <br/>
        {{ this.action.action }} <br/>

      </div>
       <div class="col">
        <button type="button" class="btn btn-primary">Action</button> <br/>
        Action: {{ this.action.action }} <br/>
        Reward: {{ this.action.reward }} <br/>
      </div>
      <div class="col">
        <button type="button" class="btn btn-primary">Next State</button>
        {{ this.action.action }}
      </div>
    </div>
     <div class="row">
      <div class="col">
        <button type="button" class="btn btn-primary"> Prev {{ this.prev }} </button>
      </div>
       <div class="col">
        <button type="button" class="btn btn-primary"> Next {{ this.next }} </button>
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
      msg: '',
      action: {},
      next: '1',
      prev: '0',
      state: {},
      nextstate: {}

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
          this.msg = 'Action ' + index + ' Ready'
          this.action = res.data.action
          this.next = res.data.next
          this.prev = res.data.prev
          this.state = res.data.action.state
          this.nextstate = res.data.action.nextstate
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
