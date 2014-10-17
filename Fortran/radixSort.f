c A program to implement Radix sort in Fortran 77
c This was done for CSC 341.
c Sorts the numbers in file "data.txt"
c By Daniel Graham
c version 1.1 10/17/2014


c Takes an array of size 101 and prepares it to act as a queue of
c integers by setting every address of the array to the value -1
c The head of the queue is not always array(1), but changes as items
c are enqueued and dequeued. The queueHead holds the index of the start
c of the queue as it changes. The last item always comes before a -1
c but theres is also a queueEnd that holds the index of the last item.
c
c Params: queue The 101 size array to use as a queue.

      subroutine initializeQueue(queueHead, queueTail, queue, queueSize)
      
      integer queue(*), queueHead, queueTail, queueSize
      queueHead = 1
      queueTail = 1
      queueSize = 0
      do 60 i = 1, 101
        queue(i) = -1
 60   continue
      return
      end

c Reads a .txt line by line for positive integers. The integers must be
c no more than 4 digits and there cannot be more than 100 positive
c integers. Increments a count of integers and inserts the integers to
c an array.
c
c Params: numElements Number of elements in the list.
c         fName File path of .txt which contains integers to add.
c         array The array that will contain integers.

      subroutine inputArray(numElements, fName, array)

      Character fName*(*)
      integer numElements, array(*)
      
      open(44, File = fName, Status = 'OLD')
      read(44, *) line
      i = 1

c The following loop iterates over the file and if the number it reaches
c is non-negative, it increments numElements and adds the number to the 
c array otherwise, it stops reading the file.

 10   if(line.GE.0) then
          numElements = numElements + 1
          array(numElements) = line
          read(44, *) line
          goto 10
      endif
      close(44)
      return
      end

c Enqueues an integer to the queue array. If the queue already has 100
c items, the subroutine sends a message. Changes the value of queueEnd 
c to match the updated end of the queue. 
c
c Params: queueTail Index of the next open space.
c         queue Array that has been initialized to a queue.
c         item Integer to add to the queue.
c         queueSize Current size of the queue

      subroutine enqueue(queueTail, queue, item, queueSize)

      integer queueTail, queue(*), item, queueSize
      
      if(queue(queueTail).NE.-1) then
        write(*,*) "Queue Full!"
      else
        queue(queueTail) = item
        queueSize = queueSize + 1
        
        if(queueTail.GE.101) then
            queueTail = 1
        else
            queueTail = queueTail + 1
        endif
        
      endif

      return
      end

c Returns the integer at the head of the queue. If the 
c queue is empty prints an error to the screen and returns -1. 
c Decrements queueSize.
c
c Params: queueHead Location of the item at the head of the queue.
c         queue The queue array to dequeue from.
c         queueSize The current size of the queue array.  
      
      integer function dequeue(queueHead, queue, queueSize)

      integer queueHead, queue(*), queueSize
      
      if(queue(queueHead).EQ.-1) then
        write(*,*) "No Items On Queue"
        dequeue = -1
      else
        dequeue = queue(queueHead)
        queue(queueHead) = -1
        queueSize = queueSize - 1
        
        if(queueHead.GE.101) then
            queueHead = 1
        else
            queueHead = queueHead + 1
        endif
        
      endif
      return
      end
      
c Uses radix sort to sort the integers in the queue by a specific place 
c (10, 100, etc.). Sorts by creating a temporary queue to sort into, 
c then returning items to the original queue in the sorted order.
c
c Params: place The place to sort by.
c         queue The queue array to sort.
c         queueHead The index of the head of the queue array.
c         queueTail Index of the next available location in queue
c         queueSize Current size of queue.

      subroutine oneSort(place, queue, queueHead, queueTail, 
     + queueSize)
     
      integer queueSort(101), queue(*)
      integer place, queueHead, queueSortHead
      integer queueTail, queueSortTail, queueSize
      integer queueSortSize, dequeueItem, modValue, dequeue, toMod
      
      call initializeQueue(queueSortHead, queueSortTail, queueSort,
     + queueSortSize)

      do 70 i = 0, 9
        do 80 j = 1, (queueSize)
            dequeueItem = dequeue(queueHead, queue, queueSize)
            toMod = dequeueItem / place
            modValue = mod(toMod,10)
            if(modValue.EQ.i) then
                call enqueue(queueSortTail, queueSort, dequeueItem, 
     + queueSortSize)
            else
                call enqueue(queueTail, queue, dequeueItem,
     + queueSize)
            endif
c This if statement determines where in the sort queue items will go

 80     continue
 70    continue
       do 90 i = 1, queueSortSize
        call enqueue(queueTail, queue, 
     + dequeue(queueSortHead, queueSort, queueSortSize),queueSize)
 90    continue
       return
       end

c Prints the queue to console in order seperated by commas.
c
c Params: queueHead The index of the head of the queue array.
c         queue The queue array to sort.
c         queueSize Current size of queue.

      subroutine printQueue(queueHead, queue, queueSize)

      integer queueHead, queueSize, queue(*), printPoint
      integer queueToPrint(101), queueToPrintHead
      integer queueToPrintTail, queueToPrintSize
      
      call initializeQueue(queueToPrintHead, queueToPrintTail, 
     + queueToPrint, queueToPrintSize)

      printPoint = queueHead
      do 110 i = 1, 100
        if(printPoint.GT.101) then
            printPoint = 1
        endif
        call enqueue(queueToPrintTail, queueToPrint,  
     + queue(printPoint), queueToPrintSize)
      printPoint = printPoint + 1
 110  continue
      write(*,*) queueToPrint
      return
      end
      
c Sorts integers in "data.txt" file using radix sort algorithm and 
c queue implementation. Cannot sort more than 100 integers and the 
c integers cannot be more than 4 digits. Prints the sorted output to 
c the screen. Ignore tailing -1s.      
      
      program radixSort
      integer queue(101), queueHead, queueTail, queueSize
      Character fileName*(100)
      
      fileName = "data.txt"
      call initializeQueue(queueHead, queueTail, queue, queueSize)
      call inputArray(queueSize, fileName, queue)
      queueTail = queueSize + 1
      
      call oneSort(1, queue, queueHead, queueTail,
     +  queueSize)
      call oneSort(10, queue, queueHead, queueTail,
     +  queueSize)
      call oneSort(100, queue, queueHead, queueTail,
     +  queueSize)
      call oneSort(1000, queue, queueHead, queueTail,
     +  queueSize)
c I could have done the above as a loop, but is clearer as is.

      call printQueue(queueHead, queue, queueSize)
      
      stop
      end
      
      
      
