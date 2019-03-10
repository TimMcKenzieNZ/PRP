import DS from 'ember-data'

export default DS.Model.extend({
  description: DS.attr('string'),
  date: DS.attr('string'),
  log: DS.attr('string'),
  author: DS.belongsTo('teammember'),
  deliverable: DS.belongsTo('deliverable')
})
