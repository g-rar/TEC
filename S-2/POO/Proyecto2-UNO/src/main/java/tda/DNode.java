package tda;

public class DNode<T> {
	private T Value	;
	private DNode<T> Next;
	private DNode<T> Prev;
	
	public DNode(T pValor) {
		Value = pValor;
	}

	public T getValue() {
		return Value;
	}

	public void setValue(T valor) {
		Value = valor;
	}

	public DNode<T> getNext() {
		return Next;
	}

	public void setNext(DNode<T> next) {
		Next = next;
	}

	public DNode<T> getPrev() {
		return Prev;
	}

	public void setPrev(DNode<T> prev) {
		Prev = prev;
	}
	
        @Override
	public String toString() {
		String returnValue = "( " + Value.toString() + " )";
		return returnValue;
	}
}
