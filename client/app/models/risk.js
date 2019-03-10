import DS from 'ember-data'

export default DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  likelihood: DS.attr('string'),
  impact: DS.attr('string'),
  flagged: DS.attr('boolean'),
  risk: DS.belongsTo('risk'),
  riskSeverity: DS.attr('string'),
  riskMitigations: DS.attr() // not specifiying a type allows you to use implicit types like arrays

})
