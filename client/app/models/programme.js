import DS from 'ember-data'

export default DS.Model.extend({
  name: DS.attr('string'),
  slug: DS.attr('string'),
  description: DS.attr('string'),
  image: DS.attr('string'),
  startDate: DS.attr('date'),
  endDate: DS.attr('date'),
  goals: DS.hasMany('goal'),
  vision: DS.attr('string')
})
