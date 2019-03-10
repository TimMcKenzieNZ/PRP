import DS from 'ember-data'

export default DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  startDate: DS.attr('date'),
  endDate: DS.attr('date'),
  progress: DS.attr('number'),
  status: DS.attr('string'),
  order: DS.attr('number'),
  deliverables: DS.hasMany('deliverable'),
  risks: DS.hasMany('risk'),
  projects: DS.hasMany('project')

})
