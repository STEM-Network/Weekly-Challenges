
#include <iostream>
#include <bitset>
#include <cstdlib>
#include <time.h>

int main() {
    int wDimension = 8;
    int hDimension = 8;
    srand(time(NULL));
    int board[wDimension][hDimension];
    for(int i = 0; i < hDimension; i++) {
        for(int j = 0; j < wDimension; j++) {
            board[i][j] = rand() % 2;
        }
    }
    std::cout << "Board where 1 is face up and 0 is a tails: " << std::endl;
    for(int i = 0; i < hDimension; i++) {
        for(int j = 0; j < wDimension; j++) {
            std::cout << board[i][j];
        }
        std::cout << std::endl;
    }
    std::cout << "Enter the spot where the key is located: ";
    int keyspot;
    std::cin >> keyspot;
    int mask;
    int counter;
    int previous = 0;
    for(int i = 0; i < hDimension; i++) {
        for(int j = 0; j < wDimension; j++) {
            if(board[i][j] == 1) {                 
                mask = previous^counter;
                previous = mask;
            }
            counter++;
        }
    }
    int flipPosition = mask^keyspot; 
    std::cout << "Prisoner 1 flip the coin in index: " << flipPosition << std::endl;
    int counter2 = 0;
    for(int i = 0; i < hDimension; i++) {
        for(int j = 0; j < wDimension; j++) {
            if(counter2 == flipPosition) {
                if(board[i][j] == 1) {
                    board[i][j] = 0;
                } else {
                    board[i][j] = 1;
                }
            }
            counter2++;
        }
    }
    std::cout << "New board:" << std::endl;
    for(int i = 0; i < hDimension; i++) {
        for(int j = 0; j < wDimension; j++) {
            std::cout << board[i][j];
        }
        std::cout << std::endl;
    }
    int secondMask;
    int secondCounter;
    int secondPrevious = 0;
    for(int i = 0; i < hDimension; i++) {
        for(int j = 0; j < wDimension; j++) {
            if(board[i][j] == 1) {                 
                secondMask = secondPrevious^secondCounter;
                secondPrevious = secondMask;
            }
            secondCounter++;
        }
    }
    std::cout << "Second prisoner XOR all the heads up coins which becomes: " << secondMask  << ". Which is where the key is located." << std::endl;
}