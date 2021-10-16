#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();

	private:
		int val;
		int _fib(int);
	};


Integer::Integer(int n){
	val = n;
	}

int Integer::fib(){
	int n = val;
	return _fib(n);
}

int Integer::_fib(int n){
	if (n  <= 1){
		return n;
	}else{
		return _fib(n-1) + _fib(n-2);
	}
}

int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	int Integer_fib(Integer* integer) {return integer->fib();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}