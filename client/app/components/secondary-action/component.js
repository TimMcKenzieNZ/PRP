import Component from '@ember/component'

export default Component.extend({
  tagName: 'button',
  classNames: 'c-secondary-action',
  actions: {
    onClick () {
      this.get('onClick')()
    }
  }
})
