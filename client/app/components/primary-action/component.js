import Component from '@ember/component'

export default Component.extend({
  tagName: 'button',
  classNames: 'c-primary-action',
  actions: {
    onClick () {
      this.get('onClick')()
    }
  }
})
