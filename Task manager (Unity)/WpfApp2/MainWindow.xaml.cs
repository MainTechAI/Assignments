using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace WpfApp2
{
    public class Process
    {
        public string Name { get; set; }
        public string CP { get; set; }
        public string RAM { get; set; }
        public string TimeStart { get; set; }
        public int Time { get; set; }
    }


   
    public partial class MainWindow : Window
    {
        Updater u = new Updater();
        List<Process> proc = new List<Process>();
        bool method = false;
        public MainWindow()
        {
            InitializeComponent();
            TimeLabel.Content = DateTime.Now.ToString();
            proc.Add(new Process { Name = "Opera", CP = "0", RAM = "450", TimeStart = DateTime.Now.ToString(), Time = 50});
            proc.Add(new Process { Name = "Visual Studio", CP = "0", RAM = "500", TimeStart = DateTime.Now.ToString(), Time = 32 });
            proc.Add(new Process { Name = "Word", CP = "0", RAM = "345", TimeStart = DateTime.Now.ToString(), Time = 10 });
            proc.Add(new Process { Name = "Photoshop", CP = "0", RAM = "650", TimeStart = DateTime.Now.ToString(), Time = 15 });
            proc.Add(new Process { Name = "Acrobat", CP = "0", RAM = "345", TimeStart = DateTime.Now.ToString(), Time = 25 });

            foreach (Process i in proc)
                ListViewMain.Items.Add(i);

            

            DispatcherTimer timer = new DispatcherTimer();
            timer.Tick += new EventHandler(timer_Tick);
            timer.Interval = new TimeSpan(0, 0, 0, 0, 1000);
            timer.Start();

        }

        private void timer_Tick(object sender, EventArgs e)
        {
            ListViewMain.Items.Clear();
            proc = u.Update(proc, method);
            foreach (Process i in proc)
                ListViewMain.Items.Add(i);
            TimeLabel.Content = DateTime.Now.ToString();
        }

        private void ButtonAdd_Click(object sender, RoutedEventArgs e)
        {
            AddWindow addWindow = new AddWindow();
            if(addWindow.ShowDialog() == true)
                proc.Add(addWindow.Data);
        }

        private void ButtonAlg1_Click(object sender, RoutedEventArgs e)
        {
            method = true;
        }

        private void ButtonAlg2_Click(object sender, RoutedEventArgs e)
        {
            method = false;
        }
    }

    class Updater
    {
        public List<Process> Update(List<Process> old, bool meth)
        {
            bool exist = false;
            bool add = false;
            List <Process> NewProc = new List<Process>();
            foreach (Process oldProc in old)
            {
                if (oldProc.Time>1)
                    if (oldProc.CP == "0")
                        NewProc.Add(new Process { Name = oldProc.Name, CP = oldProc.CP, RAM = oldProc.RAM, TimeStart = oldProc.TimeStart, Time = oldProc.Time });
                    else
                        NewProc.Add(new Process { Name = oldProc.Name, CP = oldProc.CP, RAM = oldProc.RAM, TimeStart = oldProc.TimeStart, Time = --oldProc.Time });
            }
            if (meth)
            {
                foreach (Process nProc in NewProc)
                {
                    if (nProc.CP != "0") exist = true;
                }
                if (exist == false && NewProc.Count > 0) NewProc[0].CP = "99";
            }
            else
            {
                foreach (Process nProc in NewProc)
                {
                    if (nProc.CP != "0")
                    {
                        exist = false;
                        add = true;
                        nProc.CP = "0";
                    }
                    else
                        if (add) { nProc.CP = "99"; exist = true; add = false; }
                }
                if (exist == false && NewProc.Count > 0) NewProc[0].CP = "99";

            }
            return NewProc;
        }
    }
}
