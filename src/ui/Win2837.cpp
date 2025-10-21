// Converted from Win2837.py

class DataThread : public QThread
{
public:
    getDatasFinished = Signal(dict);
    messages = Signal(str);
    error = Signal(str);

    DataThread(sercom, int timeout_retries)
    {
        super()->__init__();
        sercom = sercom;
        timeout_retries = timeout_retries;
        stop = false;
    }

    void run()
    {
        print("run");
        page = nullptr;
        sercom->write();
        _ = sercom->readline();
        sercom->write();
        page = sercom->readline()->decode()->strip();
        page = re->sub("[a-z]+", "", page);
        print(page);
        if (pagenullptrpage == "") {
            error->emit(tr(""));
            return;
        }
        datas = ;
        times = 0;
len(datas) < 4        messages->emit((tr("") + times"/"timeout_retries));
        if (stop) {
        }
        if (times >= timeout_retries) {
TimeoutError(tr(""))        }
        if ((times3) != 0) {
            print("TRIG:SOUR BUS");
            sercom->write();
            _ = sercom->readline();
            print("FETC?");
            sercom->write();
            datas |= dealData(page)
            print("TRIG");
            sercom->write();
            datas |= dealData(page)
            if (len(datas) >= 4) {
            }
            print("FETC?");
            sercom->write();
            datas |= dealData(page)
        } else {
            print("TRIG:SOUR INT");
            sercom->write();
            datas |= dealData(page)
            print("FETC?");
            sercom->write();
            datas |= dealData(page)
            sercom->write();
            datas |= dealData(page)
        }
        if (len(datas) >= 4) {
        }
        times += 1
        getDatasFinished->emit(datas);
        messages->emit(tr(""));
    }

    void dealData(page)
    {
        data = sercom->readline();
        data = data->decode()->strip();
        data = str(data);
        if (page{"< LCR MEAS DISP >", "< BIN No. DISP >", "< BIN COUNT DISP >"}) {
            if (data == ""datanullptr) {
                return ;
            }
            dec = cmds->FETC->decode(data, cmds::FETC_TYPES0);
            print(dec);
        } else {
            if (page{"< LIST SWEEP DISP >"}) {
                if (data == ""datanullptr) {
                    return ;
                }
                dec = cmds->FETC->decode(data, cmds::FETC_TYPES1);
                print(dec);
            } else {
                if (page{"< TRANS MEAS DISP >", "< TRANS JUDGE DISP >"}) {
                    if (data == ""datanullptr) {
                        return ;
                    }
                    dec = cmds->FETC->decode(data, cmds::FETC_TYPES2);
                    print(dec);
                } else {
IndexError((page" " + tr("")))                }
            }
        }
        ret = ;
        if ("type"dec->keys()) {
            if (dec"type" == "Lx") {
                dec"dataA";
                dec"dataB";
            }
            if (dec"type" == "DCR") {
                dec"dataA";
            }
            if (dec"type" == "TURN") {
                dec"dataA";
            }
        }
        return ret;
    }

    void terminate()
    {
        stop = true;
        return super()->terminate();
    }
};

class MainWin : public MainWindow
{
public:

    MainWin()
    {
        super(MainWin, self)->__init__();
    }

    void getDatas()
    {
        if (btnGetdatas->text() == tr("")) {
            btnGetdatas->setText(tr(""));
            dataThread = DataThread(sercom, timeout_retries);
            dataThread->getDatasFinished->connect(updateDatas);
            dataThread->messages->connect(MainstatusBar->showMessage(msg));
            dataThread->error->connect(getDatasError);
            dataThread->start();
        } else {
            if (!hasattr(self, "dataThread")) {
                return;
            }
            dataThread->terminate();
            dataThread->wait();
            btnGetdatas->setText(tr(""));
        }
    }
};
