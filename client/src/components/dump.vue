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
        Día: {{ this.state.dia }} Hora: {{ this.state.momentoDia }}
        Pantalla: {{ this.state.numPantalla }}<br/>
        Obsequium: {{ this.state.obsequium }} Bonus: {{ this.state.bonus }}
        Porcentaje: {{ this.state.procentaje }} <br/>
        <div v-html="html">
        </div>
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
        <button type="button" class="btn btn-primary"  @click="getAction(prev)" >
          Prev {{ this.prev }}
        </button>
      </div>
       <div class="col">
        <button type="button" class="btn btn-primary"  @click="getAction(next)" >
          Next {{ this.next }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Dump',
  data() {
    return {
      msg: '',
      action: {},
      next: '1',
      prev: '0',
      state: {},
      nextstate: {},
      html: 'tururu',
    };
  },
  methods: {
    createRejilla() {
      let html = '<table style="font-family:Courier; font-size:9px;" >';
      const rej = this.state.rejilla;

      html += '<tr><td>*</td>';
      for (let ii = 0; ii <= 23; ii += 1) {
        html += '<td><b>';
        html += String(ii);
        html += '</b></td>';
      }
      html += '</tr>';

      rej.forEach((row, y) => {
        html += '<tr><td><b>';
        html += String(y);
        html += '</b></td>';
        row.forEach((col) => {
          html += '<td style="width:7px; height:7px; background-color:rgb(0,';
          html += String(255 - (col[2] * 10));
          html += ',255);">';
          if (col[0] >= 0) {
            html += String(col[0]);
          }
          html += '</td>';
        });
        html += '<tr>';
      });
      html += '<table>';
      this.html = html;
    },
    getGame() {
      const path = 'http://localhost:5000/game';
      axios.get(path)
        .then((res) => {
          this.msg = res.data.game.filename;
          this.getAction('0');
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getAction(index) {
      let path = 'http://localhost:5000/action/';
      path += index;
      axios.get(path)
        .then((res) => {
          let tmp = 'Action ';
          tmp += ' Ready';
          this.msg = tmp;
          this.action = res.data.action;
          this.next = res.data.next;
          this.prev = res.data.prev;
          this.state = res.data.action.state;
          this.nextstate = res.data.action.nextstate;
          this.createRejilla();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getGame();
  },
};
</script>
