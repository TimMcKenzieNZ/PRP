import Component from '@ember/component'
import { set } from '@ember/object'

export default Component.extend({
  classNames: ['l-content-page'],

  selectedInitiative: null,

  hasSelectedInitiative: false,

  actions: {
    setInitiative: function (initiative) {
      set(this, 'selectedInitiative', initiative)
    },

    hasSelectedInitiative () {
      set(this, 'hasSelectedInitiative', true)
    }
  }
})
