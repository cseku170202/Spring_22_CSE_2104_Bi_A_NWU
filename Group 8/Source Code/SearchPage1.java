import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SearchPage1 implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label1 = new JLabel();
    JLabel label2 = new JLabel();
    JTextField text = new JTextField();
    JButton button = new JButton();
    int num;
    int n;
    int a[];
    int pos;
    SearchPage1(int ar[], int index){

        a = new int[index];
        n = index;
        for(int f = 0; f < index; f ++){
            a[f] = ar[f];
        }

        label1.setText("Position: ");
        label1.setVisible(true);
        label1.setBounds(30, 25, 70, 30);
        label1.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        text.setVisible(true);
        text.setBounds(110, 30, 180, 22);
        text.setPreferredSize(new Dimension(200, 30));

        button.setText("Submit");
        button.setVisible(true);
        button.setFocusable(false);
        button.setBounds(110, 55, 75, 22);
        button.setFont(new Font("Times New Roman", Font.PLAIN, 13));
        button.addActionListener(this);

        frame.setTitle("Search");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("search.png")).getImage();
        frame.setIconImage(icon);
        frame.setBounds(490, 320, 350, 180);
        frame.setLayout(null);
        frame.add(label1);
        frame.add(text);
        frame.add(button);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            pos = Integer.parseInt(text.getText());
            frame.dispose();
            if(pos > n){
                JOptionPane.showOptionDialog(null, "Position "+pos+" Not Found", "Information", JOptionPane.CLOSED_OPTION, JOptionPane.INFORMATION_MESSAGE, null, null, 0);
            }
            else {
                JOptionPane.showOptionDialog(null, "Position "+pos+" Found "+a[pos-1], "Information", JOptionPane.CLOSED_OPTION, JOptionPane.INFORMATION_MESSAGE, null, null, 0);
            }
        }
    }
}
