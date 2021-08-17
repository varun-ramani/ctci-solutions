import java.lang.Comparable;
import java.util.Comparator;
import java.util.Arrays;

class BinaryHeap {
    private Integer[] values;
    private int defaultCapacityExtension;
    private int nextIndex;
    protected Comparator<Integer> comparator;

    public BinaryHeap(int initialCapacity, Comparator<Integer> comparator) {
        this.values = new Integer[initialCapacity];
        this.defaultCapacityExtension = initialCapacity;
        this.comparator = comparator;
        this.nextIndex = 0;
    }

    protected void extendCapacity(int extendBy) {
        Integer[] newValues = new Integer[values.length + extendBy];
        for (int index = 0; index < values.length; index++) {
            newValues[index] = values[index];
        }
        values = newValues;
    }

    protected void extendCapacity() {
        extendCapacity(this.defaultCapacityExtension);
    }

    private int getParent(int childIndex) {
        return (childIndex - 1) / 2;
    } 

    private int getLeftChild(int parentIndex) {
        return (2 * parentIndex) + 1;
    }

    private int getRightChild(int parentIndex) {
        return (2 * parentIndex) + 2;
    }

    private void swapIndices(int index, int otherIndex) {
        Integer auxValue = values[index];
        values[index] = values[otherIndex];
        values[otherIndex] = auxValue;
    }
    
    protected void bubbleUp(int fromIndex) {
        while (fromIndex != 0 && comparator.compare(values[fromIndex], values[getParent(fromIndex)]) > 0) {
            swapIndices(fromIndex, getParent(fromIndex));
            fromIndex = getParent(fromIndex);
        }
    }

    protected void bubbleDown(int fromIndex) {
        int rightChild = getRightChild(fromIndex);
        int leftChild = getLeftChild(fromIndex);

        while ((values[rightChild] != null && comparator.compare(values[fromIndex], values[rightChild]) < 0)
               || (values[leftChild] != null && comparator.compare(values[fromIndex], values[leftChild]) < 0)) {
            if (values[rightChild] != null && values[leftChild] != null) {
                if (comparator.compare(values[rightChild], values[leftChild]) > 0) {
                    swapIndices(fromIndex, rightChild);
                    fromIndex = rightChild;
                } else {
                    swapIndices(fromIndex, leftChild);
                    fromIndex = leftChild;
                }
            } else if (values[rightChild] != null) {
                swapIndices(fromIndex, rightChild);
                fromIndex = rightChild;
            } else {
                swapIndices(fromIndex, leftChild);
                fromIndex = leftChild; 
            }

            leftChild = getLeftChild(fromIndex);
            rightChild = getRightChild(fromIndex);
        }
    }

    public void add(Integer newValue) {
        if (nextIndex == values.length)
            extendCapacity();
        
        values[nextIndex] = newValue;
        bubbleUp(nextIndex);
        nextIndex += 1;
    }

    public Integer remove() {
        if (isEmpty())
            return null;

        Integer returnValue = values[0];
        values[0] = values[nextIndex - 1];
        values[nextIndex - 1] = null;
        bubbleDown(0);

        nextIndex -= 1;

        return returnValue;
    }

    public boolean isEmpty() {
        return (nextIndex == 0);
    }
}

class MaxHeap extends BinaryHeap {
    public MaxHeap(int initialCapacity) {
        super(initialCapacity, new Comparator<Integer>() {
            @Override
            public int compare(Integer item1, Integer item2) {
                return item1 - item2;
            }
        });
    }
}

class MinHeap extends BinaryHeap {
    public MinHeap(int initialCapacity) {
        super(initialCapacity, new Comparator<Integer>() {
            @Override
            public int compare(Integer item1, Integer item2) {
                return item2 - item1;
            }
        });
    }
}

public class BinaryHeapImplementation {
    public static Integer[] heapSort(Integer[] originalValues, boolean ascending) {
        BinaryHeap heap = (ascending) ? new MinHeap(100) : new MaxHeap(100);
        
        for (int index = 0; index < originalValues.length; index++)
            heap.add(originalValues[index]);
        
        for (int index = 0; index < originalValues.length; index++)
            originalValues[index] = heap.remove();
        
        return originalValues;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(BinaryHeapImplementation.heapSort(new Integer[] {0, 5, -1, 20, 6}, false)));
        System.out.println(Arrays.toString(BinaryHeapImplementation.heapSort(new Integer[] {0, 5, -1, 20, 6}, true)));
    }
}