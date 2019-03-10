import { helper } from '@ember/component/helper'

/**
 * Checks if the given item is in the given list
 */
export function has ([list, item]) {
  return list.indexOf(item) >= 0
}

export default helper(has)
