import DS from 'ember-data'

export default DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  startDate: DS.attr('date'),
  endDate: DS.attr('date'),
  progress: DS.attr('number'),
  priority: DS.attr('string'),
  image: DS.attr('string'),
  goals: DS.hasMany('goal'),
  cost: DS.attr('number'),
  status: DS.attr('string'),
  initiatives: DS.hasMany('initiative'),
  roles: DS.hasMany('role')

})
