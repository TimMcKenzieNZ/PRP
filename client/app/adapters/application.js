
import DS from 'ember-data'

import config from '../config/environment'

export default DS.JSONAPIAdapter.extend({
  namespace: config.apiNamespace,
  host: config.host,
  coalesceFindRequests: true // Bundles multiple requests for all objects in a set into a single request

})
