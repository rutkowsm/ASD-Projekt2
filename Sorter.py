import FreqCounter
import HeapSort


def sortFreqArray(text):

    freqArray = FreqCounter.countCharacters(text)
    sortedFreqArray = HeapSort.heapSort(freqArray)

    return sortedFreqArray
