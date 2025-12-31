public interface Observable {
   abstract void add(Observer observer);
   abstract void remove(Observer observer);
   abstract void notif();
} 
