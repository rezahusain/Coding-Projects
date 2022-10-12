#include <cstdio>
#include <cstring>
#include <cctype>

class OperatorStack{
    private:
      int totalSize;
      int currentSize;
      char* arr;

    public:
      OperatorStack(){
        this->totalSize = 2;
        this->currentSize = 0;
        this->arr = new char[this->totalSize];
      }
      bool isEmpty(){
        return this->currentSize == 0;
      }
      bool isFull(){
        return this->currentSize == this->totalSize;
      }
      void push(char value){
        if(isFull()){
          this->totalSize = this->totalSize + 2;
          this->currentSize++;
          this->arr[this->currentSize] = value;
        }
        else{
          this->currentSize++;
          this->arr[this->currentSize] = value;
        }
      }
      char pop(){
          this->currentSize--;
          return this->arr[this->currentSize];
      }
      char top(){
        return this->arr[this->currentSize];
      }
};

class ValueStack{
    private:
      int totalSize;
      int currentSize;
      int* arr;

    public:
      ValueStack(){
        this->totalSize = 2;
        this->currentSize = 0;
        this->arr = new int[this->totalSize];
      }
      bool isEmpty(){
        return this->currentSize == 0;
      }
      bool isFull(){
        return this->currentSize == this->totalSize;
      }
      void push(int value){
        if(isFull()){
          this->totalSize = this->totalSize + 2;
          this->currentSize++;
          this->arr[this->currentSize] = value;
        }
        else{
          this->currentSize++;
          this->arr[this->currentSize] = value;
        }
      }
      int pop(){
          this->currentSize--;
          return this->arr[this->currentSize];
      }
      int top(){
        return this->arr[this->currentSize];
      }
};