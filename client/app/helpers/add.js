import { helper } from '@ember/component/helper'

export function add (params) {
  return params.reduce((acc, v) => acc + v, 0)
}

export default helper(add)
