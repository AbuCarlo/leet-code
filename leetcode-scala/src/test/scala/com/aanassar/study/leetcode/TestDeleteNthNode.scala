package com.aanassar.study.leetcode

import org.junit.runner.RunWith
import org.scalatest.Finders
import org.scalatest.FunSuite
import org.scalatest.Matchers
import org.scalatest.junit.JUnitRunner
import org.scalatest.prop.Checkers

@RunWith(classOf[JUnitRunner])
class TestDeleteNthNode extends FunSuite with Checkers with Matchers {
  /* Medium difficulty, problem 19. "Given n will always be valid."
   *
   * A better solution would have been to maintain two pointers.
   * Advance the first one until the difference between the indices
   * == n, then advance both until the second points to null. Delete
   * the node you're on.
   */

  class ListNode(var _x: Int = 0) {
    var next: ListNode = null
    var x: Int = _x
    
    override def toString() = {
      if (next == null) 
        x.toString
      else 
        s"${x}, " + next.toString
    }
  }
  
  object ListNode {
    
    def apply(values: Int*): ListNode = apply(values.toList)
    
    def apply(values: List[Int]): ListNode = values match {
      case Nil => null
      case h :: tail => {
        val node = new ListNode(h)
        node.next = apply(tail)
        node
      }
    }
    
    def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
      def recurse(current: ListNode, count: Int): Int = {
        if (current.next == null)
          1
        else {
          val nextIndex = recurse(current.next, count + 1)
          if (nextIndex == n)
            current.next = current.next.next
          nextIndex + 1
        }
      }
      
      val length = recurse(head, 0)
      if (n == length)
        head.next
      else 
        head
    }
  }
  
  test("0th element") {
    val l = ListNode(0, 1, 2, 3)
    val actual = ListNode.removeNthFromEnd(l, 0)
    actual.toString should ===("1, 2, 3")
  }
  
  test("last element") {
    val l = ListNode(0, 1, 2, 3)
    val actual = ListNode.removeNthFromEnd(l, 1)
    actual.toString should ===("0, 1, 2")
  }
  
   test("first element") {
    val l = ListNode(0, 1, 2, 3)
    val actual = ListNode.removeNthFromEnd(l, 4)
    actual.toString should ===("1, 2, 3")
  }
}