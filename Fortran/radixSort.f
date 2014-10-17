c A program to implement Radix sort in Fortran 77
c This was done for CSC 341.
c Sorts the numbers in file "data.txt"
c By Daniel Graham
c version 1.0 9/28/2014


c Takes an array of size 101 and prepares it to act as a queue of
c integers by setting every address of the array to the value -1
c The head of the queue is not always array(1), but changes as items
c are enqueued and dequeued. The queueH holds the index of the start
c of the queue as it changes. The last item always comes before a -1
c but theres is also a queueE that holds the index of the last item.
c
c Params: queue The 101 size array to use as a queue.

      subroutine initializeQueue(queue)
      integer queue(*)
      
      do 60 i = 1, 101
        queue(i) = -1
 60   continue
 
      return
      end
      
      
c Reads a filename (no longer than 100 characters) and identifies how 
c many positive integers are stored in that .txt file. The integers must
c be one line at a time, and all before the negative ending signal 
c integer. This sort only works for lists shorter than 100 integers
c so if arraySize is > 100 the program will run out of memory.
c
c Params: x The file path of the .txt file to determine size.
   
c      integer function numElements(fName)
c      Character(len = 100) fName
c      numElements = 0
c      open(44, File = fName, Status = 'OLD')
c      read(44, *) line

c The following loop iterates over the file and if the number it reaches
c is non-negative, it increments the size of the numElements, otherwise
c it ends the reading of the file.
     
c 10   if (line.GT.-1) then
c        numElements = numElements + 1
c        read(44,*) line
c        goto 10
c      endif
c
c      close(44)
c      return 
c      end
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
   
c Reads a .txt line by line for positive integers. The integers must be
c no more than 4 digits and there cannot be more than 100 positive
c integers. Increments a count of integers and inserts the integers to
c an array.
c
c Params: numElP Number of elements in the list. Should be 0 initially.
c         fName File path of .txt which contains integers to add.
c         array The array that will contain integers.

      subroutine inputArray(numElP, fName, array)

      Character(len = 100) fName
      integer numElP, array(*)
      numElP = 0
      open(44, File = fName, Status = 'OLD')
      read(44, *) line

c The following loop iterates over the file and if the number it reaches
c is non-negative, it increments numElP and adds the number to the array
c otherwise, it stops reading the file.
     
 10   if (line.GT.-1) then
        array(numElP) = line
        numElP = numElP + 1
        read(44,*) line
        goto 10
      endif
 
      close(44)
      return
      end
      
c Enqueues an integer to the queue array. If the queue already has 100
c items, the subroutine sends a message. Changes the value of queueE to
c match the updated end of the queue. 
c
c Params: qEnd Index of the next open space.
c         queue Array that has been initialized to a queue.
c         item Integer to add to the queue.
c         qSize Current size of the queue

      subroutine enqueue(qEnd, queue, item, qSize)

      integer qEnd, queue(*), item, qSize
      
      if(queue(qEnd).NE.-1) then
        write(*,*) "Queue Full!"
        
      else
        queue(qEnd) = item
        qSize = qSize + 1
        
        if(qEnd.GE.101) then
            qEnd = 1
        else
            qEnd = qEnd + 1
        endif
        
      endif
      return
      end
      
c Returns the integer at the head of the queue. If the 
c queue is empty prints an error to the screen and returns -1. 
c Decrements qSize.
c
c Params: qHead Location of the item at the head of the queue.
c         queue The queue array to dequeue from.
c         qSize The current size of the queue array.    
      
      integer function dequeue(queueStartIndex, queue, queueSize)
      
      integer queueStartIndex, queue(*), queueSize
      
      if(queue(queueStartIndex).EQ.-1) then
        write(*,*) "No Items On Queue"
        dequeue = -1
        
      else
        dequeue = queue(queueStartIndex)
        queue(queueStartIndex) = -1
        queueSize = queueSize - 1
        
        if(queueStartIndex.GE.101) then
            queueStartIndex = 1
        else
            queueStartIndex = queueStartIndex + 1
        endif
        
      endif
      
      return
      end

c Uses radix sort to sort the integers in the 
c queue by a specific place (10, 100, etc.)
c Sorts by creating a temporary queue to sort into, then returning items
c to the original queue in the sorted order.
c
c Params: m The place to sort by.
c         queue The queue array to sort.
c         queueStartIndex The index of the head of the queue array.
c         queueEndIndex Index of the next available location in queue
c         queueSize Current size of queue.
    
      subroutine oneSort(m, queue, queueStartIndex, queueEndIndex, 
     + queueSize)

      integer queueSort(101), queue(*)
      integer m, queueStartIndex, queueSortStartIndex
      integer queueEndIndex, queueSortEndIndex, queueSize
      integer queueSortSize, dequeueItem, modValue, dequeue, toMod
      call initializeQueue(queueSort)
      queueSortStartIndex = 1
      queueSortEndIndex = 1
      queueSortSize = 0
      do 70 i = 0, 9
        do 80 j = 1, (queueSize)
            dequeueItem = dequeue(queueStartIndex, queue, queueSize)
            toMod = dequeueItem / m
            modValue = mod(toMod,10)
            if(modValue.EQ.i) then
                call enqueue(queueSortEndIndex, queueSort, dequeueItem, 
     + queueSortSize)
            else
                call enqueue(queueEndIndex, queue, dequeueItem,
     + queueSize)
            endif
c      This if statement determines where in the sort queue items willgo
 80     continue
 70    continue
       do 90 i = 1, queueSortSize
        call enqueue(queueEndIndex, queue, 
     + dequeue(queueSortStartIndex, queueSort, queueSortSize),queueSize)
 90    continue
       return
       end

c Prints the queue to console in order seperated by commas.
c
c Params: queueStartIndex The index of the head of the queue array.
c         queue The queue array to sort.
c         queueSize Current size of queue.

      subroutine printQueue(queueStartIndex, queue, queueSize)
      integer queueStartIndex, queueSize, queue(*), printPoint
      integer queueToPrint(101), queueToPrintStartIndex
      integer queueToPrintEndIndex, queueToPrintSize
      call initializeQueue(queueToPrint)
      queueToPrintEndIndex = 1
      queutToPrintSize = 0
      queueToPrintStartIndex = 1
      printPoint = queueStartIndex
      do 110 i = 1, 101
        if(printPoint.GE.102) then
            printPoint = 1
        endif
        call enqueue(queueToPrintEndIndex, queueToPrint,  
     + queue(printPoint), queueToPrintSize)
      printPoint = printPoint + 1
 110  continue
      write(*,*) queueToPrint
      return
      end
      
c Sorts integers in "data.txt" file using radix sort algorithm and 
c queue implementation. Cannot sort more than 100 integers and the 
c integers cannot be more than 4 digits. Prints the sorted output to 
c the screen. 
      
      program radixSort
      integer queue(101), queueStartIndex, queueEndIndex, queueSize
      integer arraySize, dequeue
      Character(len = 100) fileName
      fileName = "data.txt"
      call initializeQueue(queue)
      queueStartIndex = 1
      queueSize = arraySize(fileName)
      call inputArray(queueSize, fileName, queue)
      queueEndIndex = queueSize + 1
      call oneSort(1, queue, queueStartIndex, queueEndIndex,
     +  queueSize)
      call oneSort(10, queue, queueStartIndex, queueEndIndex,
     +  queueSize)
      call oneSort(100, queue, queueStartIndex, queueEndIndex,
     +  queueSize)
      call oneSort(1000, queue, queueStartIndex, queueEndIndex,
     +  queueSize)
c    I would have done the above as a loop, however the loops do not
c    allow multiplication incrementation. :(
      call printQueue(queueStartIndex, queue, queueSize)
      stop
      end
      
      
      
