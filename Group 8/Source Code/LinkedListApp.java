import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class Node {
    int data;
    Node next;
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedListHolder {
    Node heads;
    public LinkedListHolder(Node head) {
        this.heads = head;
    }
}

class LinkedList {
    public Node head;
    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }

    public void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println();
    }
}

public class LinkedListApp implements ActionListener {
    JFrame frame = new JFrame("Operations");
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JTextField inputField = new JTextField();
    JButton submitButton = new JButton("Submit");
    JButton button2 = new JButton();
    JButton displayButton = new JButton("Display");
    JTextArea textArea = new JTextArea();
    // Create the linked list object
    LinkedList linkedList = new LinkedList();
    private LinkedListHolder linkedListHolder = new LinkedListHolder(linkedList.head);
    int i = 0, j = 1, num;

    public LinkedListApp() {

        label.setText("Operations: ");
        label.setVisible(true);
        label.setFont(new Font("Times New Roman", Font.BOLD, 20));
        label.setBounds(10, 10, 110, 30);

        button2.setText("< Back");
        button2.setFocusable(false);
        button2.setBounds(10, 45, 90, 30);
        button2.setVisible(true);
        button2.addActionListener(this);

        // Set up the frame
        frame.setBounds(200, 100, 900, 670);
        frame.getContentPane().setBackground(new Color(188, 194, 190));
        Image icon = new ImageIcon(this.getClass().getResource("arr.png")).getImage();
        frame.setIconImage(icon);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);
        frame.setVisible(true);

        // Add the input field
        JLabel inputLabel = new JLabel("Elements are: ");
        inputLabel.setVisible(true);
        inputLabel.setBounds(110, 90, 150, 18);
        inputLabel.setFont(new Font("Times New Roman", Font.ITALIC, 18));

        label2.setText("Element "+j+": ");
        label2.setVisible(true);
        label2.setFont(new Font("Times New Roman", Font.PLAIN, 16));
        label2.setBounds(250, 130, 90, 20);

        inputField.setVisible(true);
        inputField.setBounds(340, 128, 150, 23);
        inputField.setPreferredSize(new Dimension(200, 21));

        submitButton.setEnabled(true);
        submitButton.setVisible(true);
        submitButton.setBounds(491, 128, 75, 22);
        submitButton.setFocusable(false);
        submitButton.addActionListener(this);

        displayButton.setFocusable(false);
        displayButton.setVisible(true);
        displayButton.setEnabled(false);
        displayButton.setBounds(340, 153, 75, 20);
        displayButton.addActionListener(this);

        textArea.setEditable(false);
        textArea.setVisible(true);
        textArea.setBounds(150, 320, 600, 200);

        frame.add(inputLabel);
        frame.add(inputField);
        frame.add(textArea);
        frame.add(label);
        frame.add(label2);
        frame.add(button2);
        frame.add(submitButton);
        frame.add(displayButton);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == submitButton){
            for(i = 0; ; i ++){
                num = Integer.parseInt(inputField.getText());
                linkedList.insert(num);
                j = j + 1;
                label2.setText("Element "+j+": ");
                if(j >= 1){
                    displayButton.setEnabled(true);
                }
                textArea.append(num + " -> ");
                inputField.setText("");
            }
        }

        if(e.getSource() == button2){
            CreateList create = new CreateList();
            frame.dispose();
        }

        if(e.getSource() == displayButton){
            linkedList.display();
            HomeLinkedList homelinked = new HomeLinkedList(j-1, linkedList, linkedList.head);
            frame.dispose();
        }
    }
}
