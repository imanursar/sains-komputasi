#include <iostream>
#include <chrono>
#include <random>

int main()
{
  // construct a trivial random generator engine from a time-based seed:
  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  std::default_random_engine generator (seed);

  std::uniform_real_distribution<double> distribution (0.0,100.0);

  std::cout << "some random numbers between 0.0 and 100.0: " << std::endl;
  for (int i=0; i<10; ++i)
    std::cout << distribution(generator) << std::endl;

  return 0;
}
