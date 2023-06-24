import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class L_DeletePage2 implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JTextField txt = new JTextField();
    JButton button = new JButton();
    JFrame frm;
    private LinkedList linkedList = new LinkedList();
    private Node head;
    int n;
    L_DeletePage2(int j, LinkedList linkedLists, Node heads, JFrame frame1){
        frm = frame1;
        n = j;
        linkedList = linkedLists;
        this.head = heads;

        label.setText("Number: ");
        label.setVisible(true);
        label.setBounds(30, 25, 70, 30);
        label.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        txt.setVisible(true);
        txt.setBounds(110, 30, 180, 22);
        txt.setPreferredSize(new Dimension(200, 30));

        button.setText("Submit");
        button.setVisible(true);
        button.setFocusable(false);
        button.setBounds(110, 55, 75, 22);
        button.setFont(new Font("Times New Roman", Font.PLAIN, 13));
        button.addActionListener(this);

        frame.setTitle("Delete");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("delete.png")).getImage();
        frame.setIconImage(icon);
        frame.setBounds(490, 320, 350, 180);
        frame.setLayout(null);
        frame.add(label);
        frame.add(txt);
        frame.add(button);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            int num = Integer.parseInt(txt.getText());
            int pos;
            Node tem = head;
            int j = 1, count = 0;
            while(tem != null){
                if(tem.data == num){
                    count = 1;
                    break;
                }
                tem = tem.next;
                j = j + 1;
            }
            if(count == 0){
                frame.dispose();
                JOptionPane.showOptionDialog(null, "Not found"+num, "Information", JOptionPane.CLOSED_OPTION, JOptionPane.INFORMATION_MESSAGE, null, null, 0);
            }
            else {
                pos = j;
                Node temp = head;
                if(pos == 1){
                    int l = 1;
                    while(temp != null){
                        l = l + 1;
                        temp = temp.next;
                        if(l == 2){
                            head = temp;
                        }
                    }
                    frm.dispose();
                    HomeLinkedList homelinked = new HomeLinkedList(n-1, linkedList, linkedList.head);
                    frame.dispose();
                }
                else {
                    Node del = new Node(num);
                    int x = 1;
                    while(temp != null){
                        if(x == pos){
                            del.next = temp.next;
                        }
                        temp = temp.next;
                        x = x + 1;
                    }

                    Node tmp = head;
                    int k = 1;
                    while(tmp != null){
                        if(k == pos-1){
                            tmp.next = del.next;
                        }
                        tmp = tmp.next;
                        k = k + 1;
                    }
                    frm.dispose();
                    HomeLinkedList homelinked = new HomeLinkedList(n-1, linkedList, linkedList.head);
                    frame.dispose();
                }
            }
            Node test = head;
            while(test != null){
                System.out.print(test.data + "->");
                test = test.next;
            }
        }

    }
}
