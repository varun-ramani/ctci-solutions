from utils import *

def rm_dup_linear(head: ListNode):
    if head:
        current_node = head
        seen_nodes = set()
        seen_nodes.add(current_node.val)

        while current_node.next:
            if current_node.next.val in seen_nodes:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                seen_nodes.add(current_node.val)
    return head

def rm_dup_quad(head: ListNode):
    if head:
        curr_b = head
        while curr_b and curr_b.next:
            curr_t = curr_b
            while curr_t.next:
                if curr_t.next.val == curr_b.val:
                    curr_t.next = curr_t.next.next
                else:
                    curr_t = curr_t.next
            
            curr_b = curr_b.next

    return head

test_cases = [
    ([], "[]"),
    ([1], "[1]"),
    ([1, 1], "[1]"),
    ([1, 1, 2], "[1, 2]"),
    ([1, 2], "[1, 2]"),
    ([1, 2, 2], "[1, 2]"),
    ([1, 1, 2, 2, 3, 3, 4, 4], "[1, 2, 3, 4]")
]

for case_index, (case_input, case_output) in enumerate(test_cases):
    input_ll_linear = build_ll(case_input)
    input_ll_quad = build_ll(case_input)

    linear_output = str(ListNodeIterator(rm_dup_linear(input_ll_linear)))
    quad_output = str(ListNodeIterator(rm_dup_quad(input_ll_quad)))

    if linear_output == case_output:
        print(f"Passed case {case_index}'s linear test!")
    else:
        print(f"Failed case {case_index}'s linear test with output {linear_output} and expected output {case_output}")

    if quad_output == case_output:
        print(f"Passed case {case_index}'s quad test!")
    else:
        print(f"Failed case {case_index}'s quad test with output {quad_output} and expected output {case_output}")
    